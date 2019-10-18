from .models import UserPost
from rest_framework import serializers


class UserPostSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(
        source='author.username'
    )

    class Meta:
        model = UserPost
        fields = [
            'pk',
            'author_name',
            'title',
            'body',
        ]
