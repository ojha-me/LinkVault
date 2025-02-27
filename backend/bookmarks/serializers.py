from rest_framework import serializers
from .models import Bookmarks

class BookmarksSerializer(serializers.ModelSerializer):
    '''Bookmarks serializer'''
    class Meta:
        """ Meta class """
        model = Bookmarks
        fields = ['id', 'user', 'url', 'title', 'category', 'reminder_date', 'created_at', 'forgotten_notified']


class BookmarkListResponse(serializers.Serializer):
    total_count = serializers.IntegerField()
    bookmarks = BookmarksSerializer(many=True)