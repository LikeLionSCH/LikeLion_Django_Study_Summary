from .models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"
