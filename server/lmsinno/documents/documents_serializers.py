from rest_framework import serializers

from ..models import Document, Author, Tag, Copy, Order
from ..tags.tags_serializers import TagSerializer
from ..authors.authors_serializers import AuthorSerializer
from ..copies import copies_serializers


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
        return max(0, obj.copies_available - len(Order.objects.filter(document=obj).filter(status=0)))


class DocumentResponseSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    copes = serializers.SerializerMethodField()
    copies_available = serializers.SerializerMethodField()

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
    def get_copies_available(obj):
        return max(0, obj.copies_available - len(Order.objects.filter(document=obj).filter(status=0) - len(Copy.objects.filter(status=1))))

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
        serializer = copies_serializers.CopyDetailSerializer(copyes, many=True)
        return serializer.data