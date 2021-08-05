from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ClientSerializer
from .models import Client


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class ClientRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_url_kwarg = 'client_pk'
