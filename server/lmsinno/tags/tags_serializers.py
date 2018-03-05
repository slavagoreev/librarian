from rest_framework import serializers

from ..models import Tag, TagOfDocument


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
