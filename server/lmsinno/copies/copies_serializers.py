from rest_framework import serializers

from ..models import Copy
from ..documents.documents_serializers import DocumentSerializer


class CopyDetailSerializer(serializers.ModelSerializer):
    document = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = ('copy_id',
                  'status',
                  'place_hall_number',
                  'place_shelf_letter',
                  'document',
                  'user')

    @staticmethod
    def get_document(obj):
        serializer = DocumentSerializer(obj.document)
        return serializer.data

    # TODO Return with copy a user
    @staticmethod
    def get_user(obj):
        if obj.status == 0:
            return None
        else:
            pass


class CopySerializer(serializers.ModelSerializer):

    class Meta:
        model = Copy
        fields = ('copy_id',
                  'document',
                  'place_hall_number',
                  'place_shelf_letter')
