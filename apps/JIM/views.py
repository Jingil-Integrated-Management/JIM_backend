from rest_framework.generics import ListCreateAPIView

from .serializer import ClientSerializer, UnitSerializer
from .models import Client, Unit


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UnitListCreateAPIView(ListCreateAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
