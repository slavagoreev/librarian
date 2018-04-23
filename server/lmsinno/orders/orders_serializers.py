from rest_framework import serializers

from ..documents import documents_serializers
from ..users import users_serializers
from ..models import Order, User
from .. import const

import datetime


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id',
                  'copy',
                  'user',
                  'date_created',
                  'date_accepted',
                  'date_return',
                  'status',
                  'document')


class OrderDetailSerializer(serializers.ModelSerializer):

    overdue_sum = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    document = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('order_id',
                  'document',
                  'user',
                  'date_created',
                  'date_accepted',
                  'date_return',
                  'status',
                  'overdue_sum')

    @staticmethod
    def get_overdue_sum(obj):
        sum = 0
        if obj.status == const.OVERDUE_STATUS:
            overdue_days = (datetime.date.today() - obj.date_return).days
            sum = max(min(overdue_days * const.OVERDUE_CONST, obj.copy.document.price), 0)

        return sum

    @staticmethod
    def get_user(obj):
        return users_serializers.ShortUserSerializer(User.objects.get(pk=obj.user.pk)).data

    @staticmethod
    def get_document(obj):
        return documents_serializers.ShortDocumentSerializer(obj.document).data

