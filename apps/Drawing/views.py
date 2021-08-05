from rest_framework.generics import ListCreateAPIView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DrawingSerializer
from .models import Drawing


class DrawingListCreateAPIView(ListCreateAPIView):
    serializer_class = DrawingSerializer
    queryset = Drawing.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'client']
