from rest_framework import serializers
from ..models import LogRecord


class LogRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRecord
        fields = ('record_id',
                  'user',
                  'description',
                  'method_type',
                  'log_msg_type',
                  'params',
                  'response_status')
