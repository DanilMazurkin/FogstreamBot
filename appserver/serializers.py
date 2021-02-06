from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return User.objects.create(**validated_data)