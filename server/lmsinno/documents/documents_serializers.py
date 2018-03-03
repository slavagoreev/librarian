from rest_framework import serializers

from ..models import Document, Author, Tag, Copy
from ..tags.tags_serializers import TagSerializer
from ..authors.authors_serializers import AuthorSerializer
from ..copies.copies_serializers import CopyDetailSerializer


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
                  'is_bestseller',
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


class DocumentResponseSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    copes = serializers.SerializerMethodField()

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
                  'is_bestseller',
                  'copies_available',
                  'cover',
                  'authors',
                  'tags',
                  'copes')

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

    @staticmethod
    def get_copes(obj):
        copyes = Copy.objects.filter(document=obj)
        serializer = CopyDetailSerializer(copyes, many=True)
        return serializer.data