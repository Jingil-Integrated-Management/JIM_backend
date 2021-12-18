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
    id = IntegerField(read_only=True)
    name = CharField()
    created_at = DateField()
    is_closed = BooleanField(default=False)
    client_name = StringRelatedField(source='client')
    client = PrimaryKeyRelatedField(queryset=Client.objects.all())
    comment = CharField(required=False)
    is_outsource = BooleanField(read_only=True)

    price = SerializerMethodField(read_only=True)
    type = SerializerMethodField(read_only=True)
    part_count = SerializerMethodField(read_only=True)

    def get_price(self, obj):
        return Part.objects.filter(drawing=obj).exclude(price='').aggregate(
            total=Sum(
                Cast(F('price'), output_field=Int()) * F('quantity'))
        )['total']

    def get_type(self, obj):
        if obj.parts.first():
            return obj.parts.first().get_type()
        return None

    def get_part_count(self, obj):
        if obj.parts:
            return obj.parts.count()
        return 0


class DrawingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'
