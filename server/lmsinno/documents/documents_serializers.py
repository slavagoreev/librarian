from .. import const
from rest_framework import serializers

from ..models import Document, Author, Tag, Copy, Order
from ..tags.tags_serializers import TagSerializer
from ..authors.authors_serializers import AuthorSerializer
from ..copies import copies_serializers


class ShortDocumentSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ('document_id',
                  'title',
                  'authors',
                  'cover')

    @staticmethod
    def get_authors(obj):
        document_of_authors = Author.objects.filter(documentofauthor__document_id=obj.document_id)
        serializer = AuthorSerializer(document_of_authors, many=True)
        return serializer.data


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

    @staticmethod
    def get_copies_available(obj):
        return Copy.objects.filter(document=obj).filter(status=const.NOT_ORDERED_STATUS).count()


class DocumentResponseSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    copies = serializers.SerializerMethodField()
    copies_available = serializers.SerializerMethodField()
    copies_all = serializers.SerializerMethodField()

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
                  'copies_all',
                  'cover',
                  'authors',
                  'tags',
                  'copies')

    @staticmethod
    def get_copies_available(obj):
        return Copy.objects.filter(document=obj).filter(status=const.NOT_ORDERED_STATUS).count()

    @staticmethod
    def get_copies_all(obj):
        return Copy.objects.filter(document=obj).count()

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
    def get_copies(obj):
        copies = Copy.objects.filter(document=obj)
        serializer = copies_serializers.CopyDetailSerializer(copies, many=True)
        return serializer.data