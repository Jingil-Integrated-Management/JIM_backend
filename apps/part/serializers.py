from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField, FloatField, DateField, SerializerMethodField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import OutSource, Part, File


class OutSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutSource
        fields = '__all__'


class OutSourceReadSerializer(serializers.Serializer):
    material_price = CharField()
    milling_price = CharField()
    heat_treat_price = CharField()
    wire_price = CharField()
    material_client = StringRelatedField()
    milling_client = StringRelatedField()
    heat_treat_client = StringRelatedField()
    wire_client = StringRelatedField()


class PartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class PartSerializer(serializers.Serializer):
    id = IntegerField(read_only=True)
    division = CharField(source='division.main_division', read_only=True)
    subdivision = CharField(source='division.sub_division', read_only=True)
    drawing = CharField(source='drawing.name')
    created_at = DateField(source='drawing.created_at', read_only=True)
    x = FloatField()
    y = FloatField()
    z = FloatField()
    quantity = IntegerField()
    price = CharField()
    material = CharField(source='material.name')
    comment = CharField()
    outsource = PrimaryKeyRelatedField(
        queryset=OutSource.objects.all(), write_only=True, allow_null=True)
    outsource_info = OutSourceReadSerializer(
        source='outsource', read_only=True)
    type = SerializerMethodField()
    file = PrimaryKeyRelatedField(
        queryset=File.objects.all(), write_only=True, allow_null=True)
    file_name = StringRelatedField(source='file')

    def get_type(self, obj):
        if obj.outsource:
            return '제작'
        else:
            return '연마'

    def update(self, instance, validated_data):
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.z = validated_data.get('z', instance.z)
        instance.price = validated_data.get('price', instance.price)
        instance.division = validated_data.get('division', instance.division)
        instance.drawing_id = validated_data.get('drawing', {}).get(
            'name', instance.drawing_id)
        instance.material_id = validated_data.get('material', {}).get(
            'name', instance.material_id)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.client_id = validated_data.get('client', {}).get(
            'name', instance.client_id)
        instance.outsource = validated_data.get(
            'outsource', instance.outsource)
        instance.file = validated_data.get(
            'file', instance.file)

        instance.save()
        return instance
