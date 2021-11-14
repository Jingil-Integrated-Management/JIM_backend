from rest_framework import serializers
from rest_framework.fields import BooleanField, IntegerField, SerializerMethodField, CharField, DateField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from django.db.models import Sum

from apps.client.models import Client
from apps.part.models import Part

from .models import Drawing


class DrawingSerializer(serializers.Serializer):
    id = IntegerField(read_only=True)
    name = CharField()
    created_at = DateField(read_only=True)
    is_closed = BooleanField(default=False)
    client_name = StringRelatedField(source='client')
    client = PrimaryKeyRelatedField(queryset=Client.objects.all())
    comment = CharField(required=False)

    parts = PrimaryKeyRelatedField(many=True, read_only=True)
    price = SerializerMethodField(read_only=True)
    type = SerializerMethodField(read_only=True)

    def get_price(self, obj):
        return Part.objects.filter(drawing=obj).aggregate(
            Sum('price'))['price__sum']

    def get_type(self, obj):
        if obj.parts.first():
            return obj.parts.first().get_type()
        return None

    def create(self, validated_data):
        return Drawing(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created_at = validated_data.get(
            'created_at', instance.created_at)
        instance.is_closed = validated_data.get(
            'is_closed', instance.is_closed)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.client = validated_data.get('client', instance.client)

        instance.save()
        return instance


class DashboardSerializer(serializers.Serializer):
    client = CharField(read_only=True)
    drawings = DrawingSerializer(many=True, read_only=True)
