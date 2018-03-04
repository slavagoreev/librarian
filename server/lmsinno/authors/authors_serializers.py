from rest_framework import serializers

from ..models import Author, DocumentOfAuthor


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
