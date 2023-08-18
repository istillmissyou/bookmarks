from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import SerializerMethodField

from .models import User


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )
