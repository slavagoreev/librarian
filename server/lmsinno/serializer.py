from rest_framework import serializers
from .models import Document, User, Author, DocumentOfAuthor, Order


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('document_id',
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
                  'email',
                  'password',
                  'password_salt',
                  'role',
                  'first_name',
                  'last_name',
                  'address',
                  'phone')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id',
                  'name')


class DocumentOfAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentOfAuthor
        fields = ('id',
                  'document_id',
                  'author_id')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id',
                  'document',
                  'user',
                  'data_created',
                  'data_accepted',
                  'status')
