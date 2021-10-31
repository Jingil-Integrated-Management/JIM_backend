from django.db.models.fields import TextField
from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField, FloatField, DateField
from .models import OutSource, Part


class OutSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutSource
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    division_name = CharField(
        source='division.get_full_division', read_only=True)
    drawing_file = CharField(source='get_file', read_only=True)
    created_at = CharField(source='drawing.created_at', read_only=True)
    outsource_info = OutSourceSerializer(source='outsource', read_only=True)

    class Meta:
        model = Part
        fields = '__all__'

class PartListSerializer(serializers.Serializer):
    id = IntegerField(read_only=True)
    division = CharField(source="division.main_division", read_only=True)
    subdivision = CharField(source="division.sub_division", read_only=True)
    created_at = DateField(read_only=True)
    x = FloatField(read_only=True)
    y = FloatField(read_only=True)
    z = FloatField(read_only=True)
    quantity = IntegerField(read_only=True)
    price = CharField(read_only=True)
    comment = CharField(read_only=True)
    outsource_info = OutSourceSerializer(source='outsource', read_only=True)

