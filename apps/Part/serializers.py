from rest_framework import serializers
from rest_framework.fields import CharField
from .models import Part


class PartSerializer(serializers.ModelSerializer):
    division_name = CharField(
        source='division.get_full_division', read_only=True)
    drawing_name = CharField(source='drawing.name', read_only=True)
    created_at = CharField(source='drawing.created_at', read_only=True)

    class Meta:
        model = Part
        fields = '__all__'
