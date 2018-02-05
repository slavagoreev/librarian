from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Document, User, Author, DocumentOfAuthor, Order, Copy, Tag, TagOfDocument

class DocumentSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    
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
                  'authors')


    @staticmethod
    def get_authors(obj):
        documents_of_author = DocumentOfAuthor.objects.filter(document_id=obj.document_id)
        authors = []
        for author in documents_of_author:
            author_obj = Author.objects.filter(author_id=author.author_id).first()
            authors.append(author_obj)
        return [AuthorSerializer(author).data for author in authors]


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
                  'phone',)
        
    def get_authors(self, obj):
        "obj is a Author instance. Returns list of dicts"""
        documentsOfAuthor = DocumentOfAuthor.objects.filter(document_id=obj.document_id)
        authors = []
        for author in documentsOfAuthor:
            author_obj = Author.objects.filter(author_id=author.author_id).first()
            authors.append(author_obj)
        return [AuthorSerializer(m).data for m in authors]


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
        fields = ('user_id',
                  'email',
                  'password',
                  'password_salt',
                  'role',
                  'first_name',
                  'last_name',
                  'address',
                  'phone')



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
