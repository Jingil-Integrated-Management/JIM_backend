from rest_framework import serializers
from rest_framework.fields import CharField
from .models import OutSource, Part


class OutSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutSource
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    division_name = CharField(
        source='division.get_full_division', read_only=True)
    drawing_file = CharField(source='drawing.get_file', read_only=True)
    created_at = CharField(source='drawing.created_at', read_only=True)
    type = CharField(source='get_type', read_only=True)
    outsource_info = OutSourceSerializer(source='outsource', read_only=True)

    class Meta:
        model = Part
        fields = '__all__'
