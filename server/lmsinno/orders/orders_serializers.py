from rest_framework import serializers

from ..models import Order

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

    class Meta:
        model = Order
        fields = ('order_id',
                  'copy',
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
