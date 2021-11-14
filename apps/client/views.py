from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import filters

from .serializers import ClientSerializer, ClientNameSerializer
from .models import Client


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class ClientRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_url_kwarg = 'client_pk'


class ClientNameListAPIView(ListAPIView):
    queryset = Client.objects.filter(is_pinned=True)
    serializer_class = ClientNameSerializer
    pagination_class = None
