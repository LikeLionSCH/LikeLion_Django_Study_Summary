from .models import File
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source="author.username")
    files = serializers.FileField(use_url=True)

    class Meta:
        model = File
        fields = ('pk', 'author_name', 'files', 'desc')
