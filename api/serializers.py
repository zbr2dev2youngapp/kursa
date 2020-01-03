from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'firstName',
            'lastName',
            'groupName',
        ]


class TimerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerType
        fields = [
            'id',
            'name'
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'id',
            'name'
]


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = [
            'id',
            'name',
            'active',
            'type',
            'subject',
            'duration',
            'created'
]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
