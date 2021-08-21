from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PartSerializer
from .models import Part


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
