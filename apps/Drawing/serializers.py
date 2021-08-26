from rest_framework import serializers
from .models import Drawing

from apps.Part.serializers import PartSerializer


class DrawingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drawing
        fields = '__all__'


class DrawingRetreiveUpdateSerializer(serializers.ModelSerializer):
    part = PartSerializer(source='parts', many=True, read_only=True)

    class Meta:
        model = Drawing
        fields = '__all__'
