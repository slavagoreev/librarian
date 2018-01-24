from .models import Document, Author, DocumentOfAuthor
from .serializer import DocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class DocumentDetail(APIView):
    # TODO AUTHORIZATION
    @staticmethod
    def get(request, document_id):
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
        author_name = request.GET.get('author_name', None)
        title = request.GET.get('title', None)
        year = request.GET.get('year', None)
        tag_ids = request.GET.get('tag_ids', None)
        size = request.GET.get('size', None)
        offset = request.GET.get('offset', None)

        data = Document.objects.all()

        if author_name is not None:
            data = data.filter(documentofauthor__author__name__icontains=author_name)
        if title is not None:
            data = data.filter(title__icontains=title)
        if year is not None:
            data = data.filter(year=year)
        if year is not None:
            data = data.filter(year=year)

        serializer = DocumentSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
