from django.db.models import query
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from apps.drawing.models import Drawing

from .serializers import ClientSerializer, ClientNameSerializer, ClientDashboardSerializer
from .models import Client


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all().order_by('name', 'id')
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['is_pinned']
    search_fields = ['name', ]
    pagination_class = None


class ClientRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_url_kwarg = 'client_pk'


class ClientNaviListAPIView(ListAPIView):
    queryset = Client.objects.all().exclude(
        is_pinned=0).order_by('-is_pinned', 'name')
    serializer_class = ClientNameSerializer
    pagination_class = None


class DashboardClientListAPIView(ListAPIView):
    queryset = Client.objects.filter(drawings__in=(
        Drawing.objects.prefetch_related(
            'client').filter(is_closed=False))).distinct()
    serializer_class = ClientDashboardSerializer
    pagination_class = None
