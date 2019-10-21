from .models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source="author.username")
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')
