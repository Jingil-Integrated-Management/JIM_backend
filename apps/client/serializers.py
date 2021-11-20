from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientNameSerializer(serializers.Serializer):
    id = IntegerField()
    name = CharField()
    is_pinned = IntegerField()
