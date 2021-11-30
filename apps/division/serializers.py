from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField
from .models import Division


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'


class MainDivisionSerializer(serializers.Serializer):
    id = IntegerField()
    main_division = CharField()
