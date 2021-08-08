from rest_framework import serializers
from rest_framework.fields import CharField
from .models import Part


class PartSerializer(serializers.ModelSerializer):
    division_name = CharField(source='division.get_full_division')
    drawing_name = CharField(source='drawing.name', required=False)
    created_at = CharField(source='drawing.created_at')

    class Meta:
        model = Part
        fields = ('id', 'x', 'y', 'z', 'price', 'material', 'comment',
                  'material', 'division_name', 'drawing_name', 'created_at')
