from .. import misc
from rest_framework import serializers

from ..models import Copy, Order
from ..documents import documents_serializers
from ..users import users_serializers


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
        serializer = documents_serializers.DocumentSerializer(obj.document)
        return serializer.data

    # TODO Return with copy a user
    @staticmethod
    def get_user(obj):
        if obj.status == misc.NOT_ORDERED_STATUS:
            return None
        else:
            orders = Order.objects.filter(copy=obj)
            for order in orders:
                if order.status != misc.CLOSED_STATUS:
                    return users_serializers.UserResponseDataSerializer(order.user).data


class CopySerializer(serializers.ModelSerializer):

    class Meta:
        model = Copy
        fields = ('copy_id',
                  'document',
                  'place_hall_number',
                  'place_shelf_letter')
