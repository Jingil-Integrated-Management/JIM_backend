from rest_framework import serializers
from rest_framework.fields import (BooleanField,
                                   IntegerField,
                                   SerializerMethodField,
                                   CharField,
                                   DateField,
                                   )
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField

from django.db.models import Case, When, Sum, F, IntegerField as Int
from django.db.models.functions import Cast

from apps.client.models import Client
from apps.part.models import Part

from .models import Drawing


class DrawingReadSerializer(serializers.Serializer):
    id = IntegerField()
    name = CharField()
    created_at = DateField()
    comment = CharField(required=False)
    is_outsource = BooleanField()
    client = PrimaryKeyRelatedField(read_only=True)
    client__name = StringRelatedField(source='client')
    price = SerializerMethodField()
    part_count = SerializerMethodField()
    is_closed = BooleanField()

    def get_price(self, obj):
        return Part.objects.filter(drawing=obj).exclude(price='').exclude(price=None).aggregate(
            total=Sum(
                Cast(F('price'), output_field=Int()) * F('quantity'))
        )['total']

    def get_part_count(self, obj):
        if obj.parts:
            return obj.parts.count()
        return 0


class DrawingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'
