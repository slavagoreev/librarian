from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..permissions import permission_0, permission_2, permission_3, permission_1

from .copies_serializers import CopySerializer, CopyDetailSerializer
from .. import const
from ..models import Copy, Document, Order


class CopyDetail(APIView):
    """
    Class handle with copies
    """

    @staticmethod
    @permission_1
    def get(request, copy_id):
        """
        Get Copy bi ID
        :param request:
        :param copy_id:
        :return: HTTP_200_OK and JSON-Copy: copy with such ID exists
                 HTTP_404_NOT_FOUND and JSON: copy with with such ID does not exist
        """

        result = {'status': '', 'data': {}}

        try:
            copy = Copy.objects.get(pk=copy_id)
        except Copy.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = CopyDetailSerializer(copy)

        result['data'] = serializer.data

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    @permission_2
    def post(request):
        """
        Add one particular copy
        :param request:
        :return: HTTP_200_OK and JSON-Copy: if copy was added successfully
                 HTTP_400_BAD_REQUEST: if format of input is wrong
        """

        result = {'status': '', 'data': {}}

        serializer = CopySerializer(data=request.data)

        if serializer.is_valid():
            copy = serializer.save()
            Order.queue_validation()

            document = Document.objects.get(pk=copy.document_id)
            document.copies_available = Copy.objects.filter(document=document).filter(status=const.NOT_ORDERED_STATUS).count()
            document.save()

            result['data'] = CopyDetailSerializer(Copy.objects.get(pk=copy.pk)).data

            return Response(result, status=status.HTTP_200_OK)

        result['data'] = serializer.errors

        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @permission_3
    def delete(request, copy_id):
        """
        Delete Copy bi ID
        :param request:
        :param copy_id: document id in real
        :return: HTTP_200_OK and JSON-Copy: if deleted
                 HTTP_404_NOT_FOUND: no copes or document DoesNotExist
        """

        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(document_id=copy_id)
            copies = Copy.objects.filter(document=document).filter(status=const.NOT_ORDERED_STATUS)

            if not copies:
                result['data'] = 'no copy to delete'
                return Response(result, status=status.HTTP_404_NOT_FOUND)

            copy = copies.first()
            copy.delete()
            document.copies_available -= 1
            document.save()

        except Document.DoesNotExist:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        return Response(result, status=status.HTTP_200_OK)