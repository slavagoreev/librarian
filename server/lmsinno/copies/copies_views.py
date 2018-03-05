from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .copies_serializers import CopySerializer, CopyDetailSerializer
from .. import misc
from ..models import Copy, Document
from ..permissions import LibrariantPermission


class CopyDetail(APIView):
    permission_classes = (LibrariantPermission,)
    """
    Class handle with copies
    """

    @staticmethod
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

            document = Document.objects.get(pk=copy.document_id)
            document.copies_available += 1
            document.save()

            result['status'] = misc.HTTP_200_OK
            result['data'] = CopyDetailSerializer(Copy.objects.get(pk=copy.pk)).data

            return Response(result, status=status.HTTP_200_OK)

        result['status'] = misc.HTTP_400_BAD_REQUEST
        result['data'] = serializer.errors

        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
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
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        serializer = CopyDetailSerializer(copy)

        result['status'] = misc.HTTP_200_OK
        result['data'] = serializer.data

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, copy_id):
        """
        Delete Copy bi ID
        :param request:
        :param copy_id:
        :return: HTTP_200_OK and JSON-Copy: if deleted
                 HTTP_404_NOT_FOUND: no copes or document DoesNotExist
        """

        result = {'status': '', 'data': {}}

        try:
            document = Document.objects.get(document_id=copy_id)
            copies = Copy.objects.filter(document=document).filter(status=0)
            if not copies:
                raise FileNotFoundError

            copy = copies.first()
            copy.delete()

        except Document.DoesNotExist:
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        except FileNotFoundError:
            result['status'] = misc.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        result['status'] = misc.HTTP_200_OK
        return Response(result, status=status.HTTP_200_OK)