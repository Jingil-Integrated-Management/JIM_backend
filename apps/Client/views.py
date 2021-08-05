from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ClientSerializer
from .models import Client


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
