from rest_framework import serializers
from .models import User


class UserModelSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)
