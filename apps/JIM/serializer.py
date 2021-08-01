from rest_framework import serializers
from .models import Client, Unit


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'

    def get_material(self, obj):
        return self.get_material_display()
