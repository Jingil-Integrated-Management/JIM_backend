import itertools
import operator

from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import filters
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DrawingReadSerializer, DrawingWriteSerializer
from .models import Drawing
from .filters import DrawingFilter


class DrawingListCreateAPIView(ListCreateAPIView):
    queryset = Drawing.objects.filter(
        is_closed=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = DrawingFilter
    search_fields = ['name', 'client__name']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DrawingWriteSerializer
        else:
            return DrawingReadSerializer


class DrawingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Drawing.objects.all()
    lookup_url_kwarg = 'drawing_pk'

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return DrawingWriteSerializer
        else:
            return DrawingReadSerializer


class DashboardAPIView(ListAPIView):
    pagination_class = None
    serializer_class = DrawingReadSerializer
    queryset = Drawing.objects.filter(
        is_closed=False).order_by('client', '-created_at')

    def group_by_client(self, data):
        data = sorted(data, key=operator.itemgetter('client_name'))
        data = itertools.groupby(data, key=operator.itemgetter('client_name'))

        result = list()
        for client, drawings in data:
            result.append({'client': client, 'drawings': list(drawings)})

        return result

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        self.group_by_client(serializer.data)
        return Response(self.group_by_client(serializer.data))
