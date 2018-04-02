from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .tags_serializers import TagSerializer
from ..models import Tag
from .. import const


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
        :return: HTTP_200_OK and JSON-tag: if tag with such ID exists
                 HTTP_404_NOT_FOUND and JSON: if tag with such does not exist
        """

        result = {'status': '', 'data': {}}

        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        tag_serializer = TagSerializer(tag)
        result['data'] = tag_serializer.data
        result['status'] = const.HTTP_200_OK

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
            result['status'] = const.HTTP_404_NOT_FOUND
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        tags_serializer = TagSerializer(tags_query_set, many=True)
        result['data'] = tags_serializer.data
        result['status'] = const.HTTP_200_OK

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
            result['status'] = const.HTTP_400_BAD_REQUEST
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        tag_query_set = Tag.objects.filter(name__iexact=name)

        if tag_query_set:
            result['status'] = const.HTTP_409_CONFLICT
            return Response(result, status=status.HTTP_409_CONFLICT)

        tag = Tag.objects.create(name=name)
        result['status'] = const.HTTP_201_CREATED
        result['data']['tag_id'] = tag.tag_id

        return Response(result, status=status.HTTP_201_CREATED)
