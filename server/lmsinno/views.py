from .models import Document, Author, DocumentOfAuthor
from .serializer import DocumentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .misc import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED


class DocumentDetail(APIView):
    # TODO AUTHORIZATION
    @staticmethod
    def get(request, document_id):
        """
        GET request to get one particular document
        :param request:
        :param document_id:
        :return: JSON-Document and 200 if Document exists otherwise empty JSON and 404
        """
        try:
            data = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DocumentsByCriteria(APIView):
    # TODO AUTHORIZATION
    @staticmethod
    def get(request):
        """
        GET request to get set of document by criteria
        :param request:
        :return: JSON-Documents and 200 if Documents with such criteria exists
                 otherwise empty JSON and 404
        """
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
        if size is not None and offset is not None:
            data_query_set = data_query_set.filter()[int(offset):int(offset) + int(size)]

        serializer = DocumentSerializer(data_query_set, many=True)

        print(tag_ids, file=open('log.txt', 'w'))

        result = {'status': '', 'data': serializer.data}

        if serializer.data:
            result['status'] = HTTP_200_OK
            return Response(result, status=status.HTTP_200_OK)

        result['status'] = HTTP_404_NOT_FOUND
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def post(request):
        print(request.data, file=open('log.txt', 'w'))

        author_name = request.GET.get('author_name')
        title = request.GET.get('title')
        year = request.GET.get('year')
        tag_ids = request.GET.get('tag_ids')
        description = request.GET.get('description')
        document_type = request.GET.get('type')
        price = request.GET.get('price')
        is_reference = request.GET.get('is_reference')
        copies_available = request.GET.get('copies_available')

        # document = Document(author_name, title, year, tag_ids, description,
        #                    document_type, price, is_reference, copies_available)

        serializer = DocumentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            result = {'status': HTTP_201_CREATED, 'data': serializer.data}
            return Response(request, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
