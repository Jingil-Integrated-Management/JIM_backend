from rest_framework.generics import ListCreateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PartSerializer
from .models import Part


class PartListCreateAPIView(ListCreateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division', 'drawing__client']
