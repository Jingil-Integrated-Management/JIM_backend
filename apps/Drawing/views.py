from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DrawingSerializer, DrawingRetreiveUpdateSerializer
from .models import Drawing


class DrawingListCreateAPIView(ListCreateAPIView):
    serializer_class = DrawingSerializer
    queryset = Drawing.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'client']
    search_fields = ['name', 'client__name']


class DrawingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DrawingRetreiveUpdateSerializer
    queryset = Drawing.objects.all()
    lookup_url_kwarg = 'drawing_pk'

class DashboardAPIView(ListAPIView):
    serializer_class = DrawingRetreiveUpdateSerializer
    queryset = Drawing.objects.filter(is_closed=False).order_by('client', 'created_at')