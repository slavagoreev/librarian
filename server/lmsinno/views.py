import datetime
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from lmsinno.permissions import DocumentPermission
from .models import Document, Author, DocumentOfAuthor, Tag, TagOfDocument, User, Order
from .serializer import DocumentSerializer, TagSerializer, UserSerializer, OrderSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .misc import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, \
    HTTP_409_CONFLICT

import re


class DocumentDetail(APIView):
    """
    Class to get one particular document by id
    """

    # TODO AUTHORIZATION
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
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentSerializer(document)
        result['status'] = HTTP_200_OK
        result['data'] = serializer.data

        return Response(result, status=status.HTTP_200_OK)


class DocumentsByCriteria(APIView):
    """
    Class to work with document using some criteria
    """

    permission_classes = (DocumentPermission,)

    # TODO AUTHORIZATION
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
            result['status'] = HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)

        result['status'] = HTTP_404_NOT_FOUND
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

            return Response({'status': HTTP_202_ACCEPTED, 'data': {'document_id': doc_obj.document_id}},
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
                return Response({'status': HTTP_404_NOT_FOUND, 'data': {}}, status=status.HTTP_404_NOT_FOUND)
            serializer = DocumentSerializer(document)
            document.delete()
            return Response({'status': HTTP_200_OK, 'data': serializer.data})
        else:
            return Response({'status': HTTP_400_BAD_REQUEST, 'data': {}}, status=status.HTTP_400_BAD_REQUEST)

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
                result['status'] = HTTP_404_NOT_FOUND
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

            result['status'] = HTTP_202_ACCEPTED
            result['data'] = document_serializer.data
            return Response(result, status=status.HTTP_202_ACCEPTED)

        result['status'] = HTTP_400_BAD_REQUEST
        return Response(result, status=status.HTTP_400_BAD_REQUEST)


class TagDetail(APIView):
    """
    Class to get one particular tag by ID
    """

    @staticmethod
    def get(request, tag_id):
        """
        Get one particular tag by ID
        :param request:
        :param tag_id:
        :param format:
        :return: HTTP_200_OK and JSON-tag: if tag with such ID exists
                 HTTP_404_NOT_FOUND and JSON: if tag with such doesn`t exist
        """

        result = {'status': '', 'data': {}}

        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        tag_serializer = TagSerializer(tag)
        result['data'] = tag_serializer.data
        result['status'] = HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)


class TagByCriteria(APIView):
    """
    Class to get all tags with size limit
    """

    @staticmethod
    def get(request):
        """
        Get set of tag with limited size
        :param request:
        :return: HTTP_200_OK and JSON-tags
        """

        DEFAULT_SIZE = 50
        DEFAULT_OFFSET = 0

        result = {'status': '', 'data': {}}

        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        tags_query_set = Tag.objects.all()

        size = size if size else DEFAULT_SIZE
        offset = offset if offset else DEFAULT_OFFSET
        tags_query_set = tags_query_set.filter().order_by('name')[int(offset): int(offset) + int(size)]

        if not tags_query_set:
            result['status'] = HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        tags_serializer = TagSerializer(tags_query_set, many=True)
        result['data'] = tags_serializer.data
        result['status'] = HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        """
        Add one particular tag
        :param request:
        :return: HTTP_202_ACCEPTED and JSON-tag: if tag was added successfully
                 HTTP_409_CONFLICT and JSON: if tag with such name already exists
                 HTTP_400_BAD_REQUEST: if format of input is wrong
        """

        result = {'status': '', 'data': {}}

        name = request.POST.get('name', None)

        if not name:
            result['status'] = HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        tag_query_set = Tag.objects.filter(name__iexact=name)

        if tag_query_set:
            result['status'] = HTTP_409_CONFLICT
            return Response(result, status=status.HTTP_409_CONFLICT)

        tag = Tag.objects.create(name=name)
        result['status'] = HTTP_201_CREATED
        result['data']['tag_id'] = tag.tag_id

        return Response(result, status=status.HTTP_201_CREATED)


class Booking(APIView):
    """
    Class to book one particular document by ID
    """

    @staticmethod
    def get(request, document_id):
        """
        Book one particular document by ID
        :param request:
        :param document_id:
        :param format:
        :return: HTTP_200_OK and JSON-tag: if tag with such ID exists
                 HTTP_404_NOT_FOUND and JSON: if tag with such doesn`t exist
        """

        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(pk=document_id)

            if document.copies_available == 0:
                result['status'] = HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'document is not available'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif document.is_reference:
                result['status'] = HTTP_400_BAD_REQUEST
                result['data'] = {'details': 'reference document cannot be checked out.'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            token = re.split(' ', request.META['HTTP_AUTHORIZATION'])[1]
            user = Token.objects.get(key=token).user

            order = Order.objects.create(
                document=document,
                user=user,
                status=1,
            )

        except Document.DoesNotExist:
            result['status'] = HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        document.copies_available -= 1
        document.save()

        order_serializer = OrderSerializer(order)
        result['data'] = order_serializer.data
        result['status'] = HTTP_200_OK

        return Response(result, status=status.HTTP_200_OK)


class Authorization(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):

        result = {'status': '', 'data': {}}
        try:
            email = request.META['HTTP_EMAIL']
            password = request.META['HTTP_PASSWORD']
            users = User.objects
            user = users.filter(email=email, password=password)

            if user.exists():  # if exists all good

                result['status'] = 'HTTP_202_ACCEPTED'
                result['data'] = {'token': Token.objects.get(user=user.get()).key}
                return Response(result, status=status.HTTP_202_ACCEPTED)

        except KeyError:
            pass

        result['status'] = 'HTTP_404_NOT_FOUND'
        return Response(result, status=status.HTTP_404_NOT_FOUND)


class Registration(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):

        result = {'status': '', 'data': {}}

        try:
            serialized = UserSerializer(data=request.data)

            if serialized.is_valid():
                serialized.save()
                new_user = serialized.instance

                result['status'] = 'HTTP_201_CREATED'
                result['data'] = {
                    'user_id': new_user.pk,
                    'token': Token.objects.get(user=new_user).key
                }

                return Response(result, status=status.HTTP_201_CREATED)
        except IntegrityError:
            pass

        result['status'] = 'HTTP_400_BAD_REQUEST'
        return Response(result, status=status.HTTP_400_BAD_REQUEST)