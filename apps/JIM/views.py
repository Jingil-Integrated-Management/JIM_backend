from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializer import (ClientSerializer, UnitSerializer,
                         DivisionSerializer, DrawingSerializer)
from .models import Client, Unit, Division, Drawing


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UnitListCreateAPIView(ListCreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division', 'client']


class DrawingListCreateAPIView(ListCreateAPIView):
    serializer_class = DrawingSerializer
    queryset = Drawing.objects.all()


class DivisionListCreateAPIView(ListCreateAPIView):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()
