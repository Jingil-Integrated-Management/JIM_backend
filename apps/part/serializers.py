from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import (CharField,
                                   IntegerField,
                                   FloatField,
                                   DateField,
                                   SerializerMethodField,
                                   )
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Material, OutSource, Part, File


class OutSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutSource
        fields = '__all__'


class OutSourceReadSerializer(serializers.Serializer):
    material_price = CharField()
    milling_price = CharField()
    heat_treat_price = CharField()
    wire_price = CharField()
    material_client = StringRelatedField()
    milling_client = StringRelatedField()
    heat_treat_client = StringRelatedField()
    wire_client = StringRelatedField()


class PartWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class PartReadSerializer(serializers.Serializer):
    id = IntegerField(read_only=True)
    division = CharField(source='division.main_division', read_only=True)
    subdivision = CharField(source='division.sub_division', read_only=True)
    drawing = CharField(source='drawing.name', read_only=True)
    created_at = DateField(source='drawing.created_at', read_only=True)
    x = FloatField()
    y = FloatField()
    z = FloatField()
    quantity = IntegerField()
    price = CharField()
    material = CharField(source='material.name')
    comment = CharField()
    outsource = PrimaryKeyRelatedField(
        queryset=OutSource.objects.all(), write_only=True, allow_null=True)
    outsource_info = OutSourceReadSerializer(
        source='outsource', read_only=True)
    type = SerializerMethodField()
    file = PrimaryKeyRelatedField(
        queryset=File.objects.all(), write_only=True, allow_null=True)
    file_name = StringRelatedField(source='file')

    def get_type(self, obj):
        if obj.outsource:
            return '제작'
        else:
            return '연마'


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'
