from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import OS_PartSerializer, PartSerializer
from .models import OS_Part, Part


class PartListCreateAPIView(ListCreateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division', 'client']


class PartRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
    lookup_url_kwarg = 'part_pk'


class OSPartListCreateAPIView(PartListCreateAPIView):
    serializer_class = OS_PartSerializer
    queryset = OS_Part.objects.all()


class OSPartRetrieveUpdateDestroyAPIView(PartRetrieveUpdateDestroyAPIView):
    serializer_class = OS_PartSerializer
    queryset = OS_Part.objects.all()
