from rest_framework import serializers
from django.contrib.auth.models import User


class PasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
