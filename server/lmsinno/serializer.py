from rest_framework import serializers
from rest_framework.fields import IntegerField

from .models import Document, User, Author, DocumentOfAuthor, Order, Copy, Tag, TagOfDocument


class DocumentSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

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
                  'cover',
                  'authors',
                  'tags')

    @staticmethod
    def get_authors(obj):
        document_of_authors = Author.objects.filter(documentofauthor__document_id=obj.document_id)
        serializer = AuthorSerializer(document_of_authors, many=True)
        return serializer.data

    @staticmethod
    def get_tags(obj):
        tags_of_book = Tag.objects.filter(tagofdocument__document_id=obj.document_id)
        serializer = TagSerializer(tags_of_book, many=True)
        return serializer.data


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id',
                  'name')


class DocumentOfAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentOfAuthor
        fields = ('id',
                  'document_id',
                  'author_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'password',
                  'role',
                  'first_name',
                  'last_name',
                  'address',
                  'phone',
                  'username')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id',
                  'document',
                  'user',
                  'date_created',
                  'date_accepted',
                  'date_return',
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
