from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DrawingSerializer, DrawingRetreiveUpdateSerializer
from .models import Drawing


class DrawingListCreateAPIView(ListCreateAPIView):
    serializer_class = DrawingSerializer
    queryset = Drawing.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'client']


class DrawingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DrawingRetreiveUpdateSerializer
    queryset = Drawing.objects.all()
    lookup_url_kwarg = 'drawing_pk'
