from rest_framework import serializers
from .models import Document, User, Author


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('document_id',
                  'authors',
                  'title',
                  'description',
                  'publisher',
                  'year',
                  'type',
                  'price',
                  'is_reference',
                  'copies_available')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id',
                  '')
