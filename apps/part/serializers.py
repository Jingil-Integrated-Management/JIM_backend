from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import (BooleanField, CharField,
                                   IntegerField,
                                   FloatField,
                                   DateField,
                                   SerializerMethodField,
                                   )
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from apps.client.models import Client

from .models import Material, OutSource, Part, File


class OutSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutSource
        fields = '__all__'


class OutSourceReadSerializer(serializers.Serializer):
    id = IntegerField()
    material_price = CharField()
    milling_price = CharField()
    heat_treat_price = CharField()
    wire_price = CharField()
    material_client = PrimaryKeyRelatedField(read_only=True)
    milling_client = PrimaryKeyRelatedField(read_only=True)
    heat_treat_client = PrimaryKeyRelatedField(read_only=True)
    wire_client = PrimaryKeyRelatedField(read_only=True)
    material_client__name = StringRelatedField(source='material_client')
    milling_client__name = StringRelatedField(source='milling_client')
    heat_treat_client__name = StringRelatedField(source='heat_treat_client')
    wire_client__name = StringRelatedField(source='wire_client')


class PartWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class PartReadSerializer(serializers.Serializer):
    id = IntegerField()
    x = FloatField()
    y = FloatField()
    z = FloatField()
    quantity = IntegerField()
    price = CharField()
    comment = CharField()
    drawing = PrimaryKeyRelatedField(read_only=True)
    division = PrimaryKeyRelatedField(read_only=True)
    material = PrimaryKeyRelatedField(read_only=True)
    outsource = PrimaryKeyRelatedField(read_only=True)
    file = PrimaryKeyRelatedField(read_only=True)
    created_at = DateField(source='drawing.created_at')
    client__name = CharField(source='drawing.client')
    client__id = IntegerField(source='drawing.client.id')
    drawing__is_outsource = BooleanField(source='drawing.is_outsource')
    file_name = StringRelatedField(source='file')
    division__main_division = CharField(
        source='division.main_division', read_only=True)
    division__sub_division = CharField(
        source='division.sub_division', read_only=True)
    drawing__name = StringRelatedField(source='drawing')
    drawing__is_outsource = BooleanField(source='drawing.is_outsource')
    outsource_info = OutSourceReadSerializer(
        source='outsource', read_only=True)


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'
