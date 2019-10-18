from .models import Essay
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(
        source="author.username"
    )

    class Meta:
        model = Essay
        fields = ("pk", "title", "body", "author_name")
