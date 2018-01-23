from .models import Document
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


