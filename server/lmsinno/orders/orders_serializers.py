from rest_framework import serializers

from ..users import users_serializers
from ..documents.documents_serializers import DocumentSerializer

from ..models import Order, User, Document

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
                  'status')


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
        summa = 0
        if obj.status == 2:
            overdue_days = (datetime.date.today() - obj.date_return).days
            summa = max(min(overdue_days * 100, obj.copy.document.price), 0)

        return summa

    @staticmethod
    def get_user(obj):
        return users_serializers.UserResponseDataSerializer(User.objects.get(pk=obj.user.pk)).data

    @staticmethod
    def get_document(obj):
        return DocumentSerializer(Document.objects.get(document_id=obj.copy.document.document_id)).data
