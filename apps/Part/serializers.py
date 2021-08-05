from rest_framework import serializers
from .models import Part


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Part
        fields = '__all__'

    def get_material(self, obj):
        return self.get_material_display()
