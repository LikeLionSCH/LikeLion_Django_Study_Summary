from .models import UserPost
from rest_framework import serializers


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = "__all__"
