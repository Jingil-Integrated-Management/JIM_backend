from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.db.models import Sum
from rest_framework.fields import CharField

from .models import Drawing
from apps.Part.serializers import PartSerializer
from apps.Part.models import Part


class DrawingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drawing
        fields = '__all__'


class DrawingRetreiveUpdateSerializer(serializers.ModelSerializer):
    part = PartSerializer(source='parts', many=True, read_only=True)
    price = SerializerMethodField()

    def get_price(self, obj):
        return Part.objects.filter(drawing=obj).aggregate(Sum('price'))['price__sum']

    class Meta:
        model = Drawing
        fields = '__all__'
