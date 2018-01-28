from .models import Document, Author, DocumentOfAuthor
from .serializer import DocumentSerializer, AuthorSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .misc import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED


class DocumentDetail(APIView):
    # TODO AUTHORIZATION
    def get(self, request, document_id):
        """
        GET request to get one particular document
        :param request:
        :param document_id:
        :return: JSON-Document and 200 if Document exists otherwise empty JSON and 404
        """

        result = {'status': '', 'data': {}}

        try:
            data = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentSerializer(data)
        result['status'] = HTTP_200_OK
        result['data'] = serializer.data

        return Response(result, status=status.HTTP_200_OK)


class DocumentsByCriteria(APIView):
    # TODO AUTHORIZATION
    def get(self, request):
        """
        GET request to get set of document by criteria
        :param request:
        :return: JSON-Documents and 200 if Documents with such criteria exists
                 otherwise empty JSON and 404
        """

        DEFAULT_SIZE = 50
        DEFAULT_OFFSET = 0

        result = {'status': '', 'data': {}}

        # If params are empty
        if not request.GET:
            result['status'] = HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        author_name = request.GET.get('author_name', None)
        title = request.GET.get('title', None)
        year = request.GET.get('year', None)
        tag_ids = request.GET.get('tag_ids', None)
        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        data_query_set = Document.objects

        if author_name is not None:
            data_query_set = data_query_set.filter(documentofauthor__author__name__icontains=author_name)
        if title is not None:
            data_query_set = data_query_set.filter(title__icontains=title)
        if year is not None:
            data_query_set = data_query_set.filter(year=year)
        if tag_ids is not None:
            data_query_set = data_query_set.filter(tagofdocument__tag_id__in=tag_ids)
        if size is not None or offset is not None:
            size = size if size else DEFAULT_SIZE
            offset = offset if offset else DEFAULT_OFFSET
            data_query_set = data_query_set.filter()[int(offset):int(offset) + int(size)]

        serializer = DocumentSerializer(data_query_set, many=True)

        result['data'] = serializer.data

        if serializer.data:
            result['status'] = HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)

        result['status'] = HTTP_404_NOT_FOUND
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        doc_serializer = DocumentSerializer(data=request.query_params)

        if doc_serializer.is_valid():
            doc_obj = doc_serializer.save()

            authors_list = request.GET.get('authors').replace('[', '').replace(']', '').replace('\'', '').split(', ')
            for author in authors_list:
                author_obj = Author.objects.filter(name=author).first()
                if not author_obj:
                    author_obj = Author.objects.create(name=author)
                DocumentOfAuthor.objects.create(document_id=doc_obj.document_id, author_id=author_obj.author_id)
            return Response({'status': HTTP_202_ACCEPTED, 'data': {}}, status=status.HTTP_202_ACCEPTED)

        return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
