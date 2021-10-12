from rest_framework import serializers
from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import OutSourceSerializer, PartSerializer
from .models import Part, OutSource


class OutSourceCreateAPIView(CreateAPIView):
    serializer_class = OutSourceSerializer
    queryset = OutSource.objects.all()


class PartListCreateAPIView(ListCreateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all().order_by('drawing__created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division__main_division',
                        'division__sub_division', 'client']


class PartRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
    lookup_url_kwarg = 'part_pk'
