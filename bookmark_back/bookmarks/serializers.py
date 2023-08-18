from rest_framework import serializers

from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'description', 'url', 'link_type', 'og_image', 'created_at', 'updated_at', 'user_id']


class CreateBookmarkSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)


class ResponseBookmarkSerializer(serializers.Serializer):
    error = serializers.BooleanField()
    message = serializers.CharField()
    payload = BookmarkSerializer()


class AddToCollectionSerializer(serializers.Serializer):
    bookmark_id = serializers.IntegerField(required=True)
    collection_id = serializers.IntegerField(required=True)
