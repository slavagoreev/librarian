from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .documents_serializers import DocumentSerializer
from ..models import Copy, Document, Tag, TagOfDocument, Author, DocumentOfAuthor
from ..permissions import DocumentPermission
from .. import misc

import re


class DocumentDetailByDocumentID(APIView):
    """
    Class to get one particular document by id
    """

    permission_classes = (DocumentPermission,)

    @staticmethod
    def get(request, document_id):
        """
        GET request to get one particular document
        :param request:
        :param document_id:
        :return: HTTP_200_OK and JSON-Documents: if documents with such id exists
                 HTTP_404_NOT_FOUND: if document with such id doesn`t exist
        """

        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentSerializer(document)
        result['status'] = misc.HTTP_200_OK
        result['data'] = serializer.data

        return Response(result, status=status.HTTP_200_OK)


class DocumentsByCriteria(APIView):
    """
    Class to work with document using some criteria
    """

    permission_classes = (DocumentPermission,)

    @staticmethod
    def get(request):
        """
        GET request to get set of document by criteria
        :param request:
        :return: HTTP_200_OK and JSON-Documents: if documents with such criteria exists
                 HTTP_404_NOT_FOUND: if documents with such criteria doesn`t exists
        """
        DEFAULT_SIZE = 50
        DEFAULT_OFFSET = 0

        result = {'status': '', 'data': {}}
        data_query_set = Document.objects

        author_name = request.GET.get('author_name', None)
        title = request.GET.get('title', None)
        year = request.GET.get('year', None)
        tag_ids = request.GET.get('tag_ids', None)
        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        if author_name is not None:
            author_name = author_name.strip()
            data_query_set = data_query_set.filter(documentofauthor__author__name__icontains=author_name)
        if title is not None:
            title = title.strip()
            data_query_set = data_query_set.filter(title__icontains=title)
        if year is not None:
            data_query_set = data_query_set.filter(year=year)
        if tag_ids is not None:
            tag_ids = re.sub('[ \[\]]', '', tag_ids).split(',')
            data_query_set = data_query_set.filter(tagofdocument__tag_id=tag_ids[0])
            for index in range(1, len(tag_ids)):
                data_query_set = data_query_set & data_query_set.filter(tagofdocument__tag_id=tag_ids[index])
        if size or offset:
            size = size if size else DEFAULT_SIZE
            offset = offset if offset else DEFAULT_OFFSET
            data_query_set = data_query_set.filter().order_by('-year')[int(offset):int(offset) + int(size)]
        else:
            data_query_set = data_query_set.filter().order_by('-year')

        serializer = DocumentSerializer(data_query_set, many=True)

        result['data'] = serializer.data

        if serializer.data:
            result['status'] = misc.HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)

        result['status'] = misc.HTTP_404_NOT_FOUND
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def post(request):
        """
        POST request: add one particular document
        :param request: input params
        :return: HTTP_202_ACCEPTED: if document was added successful
                 HTTP_400_BAD_REQUEST and JSON-errors: if wrong format of input data
        """

        tags_list = request.POST.get('tags', None)
        authors_list = request.POST.get('authors', None)

        doc_serializer = DocumentSerializer(data=request.data)

        if doc_serializer.is_valid() and authors_list:
            doc_obj = doc_serializer.save()

            if tags_list:
                tags_list = re.sub('[\[\]]', '', tags_list).split(',')
                for tag in tags_list:
                    tag = tag.strip()
                    tag_obj = Tag.objects.filter(name__iexact=tag).first()
                    if not tag_obj:
                        tag_obj = Tag.objects.create(name=tag)
                    TagOfDocument.objects.create(document_id=doc_obj.document_id, tag_id=tag_obj.tag_id)

            authors_list = re.sub('[\[\]]', '', authors_list).split(',')
            for author in authors_list:
                author = author.strip()
                author_obj = Author.objects.filter(name__iexact=author).first()
                if not author_obj:
                    author_obj = Author.objects.create(name=author)
                DocumentOfAuthor.objects.create(document_id=doc_obj.document_id, author_id=author_obj.author_id)

            return Response({'status': misc.HTTP_202_ACCEPTED, 'data': {'document_id': doc_obj.document_id}},
                            status=status.HTTP_202_ACCEPTED)

        return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        # TODO AUTHORIZATION
        """
        DELETE request: delete one particular document by ID
        :param request:
        :return: HTTP_200_OK: if document was deleted success
                 HTTP_404_NOT_FOUND: if document with such id not found
                 HTTP_400_BAD_REQUEST: if wrong format of input data
        """
        document_id = request.query_params.get('id')

        if document_id:
            try:
                document = Document.objects.get(pk=document_id)
            except Document.DoesNotExist:
                return Response({'status': misc.HTTP_404_NOT_FOUND, 'data': {}}, status=status.HTTP_404_NOT_FOUND)
            serializer = DocumentSerializer(document)
            document.delete()
            return Response({'status': misc.HTTP_200_OK, 'data': serializer.data})
        else:
            return Response({'status': misc.HTTP_400_BAD_REQUEST, 'data': {}}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def patch(request):
        """
        PATCH one particular document by ID
        :param request:
        :return: HTTP_202_ACCEPTED: if document was changed successfully
                 HTTP_404_NOT_FOUND: if document with such ID doesn`t exist
                 HTTP_400_BAD_REQUEST: if format of input data is wrong
        """

        result = {'status': '', 'data': {}}

        document_id = request.data.get('id', None)

        if document_id:
            try:
                document = Document.objects.get(pk=document_id)
            except Document.DoesNotExist:
                result['status'] = misc.HTTP_404_NOT_FOUND
                return Response(result, status=status.HTTP_404_NOT_FOUND)

            document_serializer = DocumentSerializer(document, data=request.data, partial=True)
            if document_serializer.is_valid():
                document_serializer.save()

            authors = request.data.get('authors', None)
            if authors:
                DocumentOfAuthor.objects.filter(document_id=document_id).delete()
                authors = re.sub('[\[\]]', '', authors).split(',')
                for author in authors:
                    author = author.strip()
                    author_obj = Author.objects.filter(name__iexact=author).first()
                    if not author_obj:
                        author_obj = Author.objects.create(name=author)
                    DocumentOfAuthor.objects.create(document_id=document.document_id, author_id=author_obj.author_id)

            tags = request.data.get('tags', None)
            if tags:
                TagOfDocument.objects.filter(document_id=document_id).delete()
                tags = re.sub('[\[\]]', '', tags).split(',')
                for tag in tags:
                    tag = tag.strip()
                    tag_obj = Tag.objects.filter(name__iexact=tag).first()
                    if not tag_obj:
                        tag_obj = Tag.objects.create(name=tag)
                    TagOfDocument.objects.create(document_id=document.document_id, tag_id=tag_obj.tag_id)

            result['status'] = misc.HTTP_202_ACCEPTED
            result['data'] = document_serializer.data
            return Response(result, status=status.HTTP_202_ACCEPTED)

        result['status'] = misc.HTTP_400_BAD_REQUEST
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetailByCopyID(APIView):
    permission_classes = (DocumentPermission,)

    @staticmethod
    def get(request, copy_id):
        result = {'status': '', 'data': {}}

        try:
            copy = Copy.objects.get(pk=copy_id)
        except Copy.DoesNotExist:
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        result['status'] = misc.HTTP_200_OK
        result['data'] = DocumentSerializer(Document.objects.get(pk=copy.document_id)).data

        return Response(result, status=status.HTTP_200_OK)
