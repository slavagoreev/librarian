from rest_framework import serializers
from .models import Document, User, Author, DocumentOfAuthor, Order, Copy, Tag, TagOfDocument


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
                  'copies_available',
                  'cover')


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
                  'date_created',
                  'date_accepted',
                  'status')


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ('copy_id',
                  'document',
                  'status',
                  'place_hall_number',
                  'place_shelf_letter')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_id',
                  'name')


class TagOfDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagOfDocument
        fields = ('document',
                  'tag')
