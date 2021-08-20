from rest_framework import serializers
from rest_framework.fields import CharField
from .models import Part, OS_Part


class PartSerializer(serializers.ModelSerializer):
    division_name = CharField(
        source='division.get_full_division', read_only=True)
    drawing_file = CharField(source='drawing.get_file', read_only=True)
    created_at = CharField(source='drawing.created_at', read_only=True)

    class Meta:
        model = Part
        fields = '__all__'


class OS_PartSerializer(PartSerializer):

    class Meta:
        model = OS_Part
        fields = '__all__'
