from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.datastructures import MultiValueDictKeyError as MVDKError

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
    pagination_class = None

    def get_queryset(self):

        try:
            query_param = self.request.query_params['client']
            queryset = Division.objects.filter(
                unit__drawing__client=query_param)
        except MVDKError:
            queryset = Division.objects.all()

        return queryset.distinct().order_by(
            'main_division', 'name', 'sub_division')
