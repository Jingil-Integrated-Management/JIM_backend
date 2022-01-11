import itertools
import operator
import calendar

from django.db.models import Sum, F, IntegerField
from django.db.models.functions import Cast

from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import filters
from rest_framework.response import Response


from django_filters.rest_framework import DjangoFilterBackend
from apps.client.models import Client

from apps.part.models import Part

from .serializers import DrawingReadSerializer, DrawingWriteSerializer, DrawingSearchSerializer
from .models import Drawing
from .filters import DrawingFilter

from utils.utils import to_int


class DrawingListCreateAPIView(ListCreateAPIView):
    queryset = Drawing.objects.all().order_by('-created_at', 'id')
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


class DrawingNameSearchAPIView(ListAPIView):
    pagination_class = None
    serializer_class = DrawingSearchSerializer
    queryset = Drawing.objects.filter(is_closed=True).values('name').distinct()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']
    search_fields = ['name', ]


class StatisticsAPIView(APIView):
    pagination_class = None

    def get(self, request):
        year, month = request.query_params['date'].split('-')
        queryset = Drawing.objects.filter(client=request.query_params['client']).filter(
            created_at__gte='{}-{}-{}'.format(year, month, '01'),
            created_at__lte='{}-{}-{}'.format(year, month,
                                              calendar.monthrange(int(year), int(month))[1])
        ).filter(is_closed=True).prefetch_related('parts')

        os_info = Part.objects.filter(drawing__is_outsource=True).exclude(price='').exclude(price=None).filter(drawing__in=queryset).aggregate(
            os_revenue=Sum(
                Cast(F('price'), output_field=IntegerField()) * F('quantity')),
            materials=Sum(Cast(F('outsource__material_price'),
                          output_field=IntegerField()) * F('quantity')),
            millings=Sum(Cast(F('outsource__milling_price'),
                         output_field=IntegerField()) * F('quantity')),
            wires=Sum(Cast(F('outsource__wire_price'),
                      output_field=IntegerField()) * F('quantity')),
            heat_treats=Sum(Cast(F('outsource__heat_treat_price'),
                            output_field=IntegerField()) * F('quantity'))
        )

        pol_info = Part.objects.filter(drawing__is_outsource=False).exclude(price='').exclude(price=None).filter(drawing__in=queryset).aggregate(
            pol_revenue=Sum(
                Cast(F('price'), output_field=IntegerField()) * F('quantity')),
        )

        result = {**os_info, **pol_info}
        result['total_revenue'] = to_int(
            result['os_revenue']) + to_int(result['pol_revenue'])
        result['total_os_costs'] = to_int(result['materials']) \
            + to_int(result['millings']) \
            + to_int(result['wires']) \
            + to_int(result['heat_treats'])
        result['os_profit'] = to_int(result['os_revenue']) \
            - to_int(result['materials']) \
            - to_int(result['millings']) \
            - to_int(result['wires']) \
            - to_int(result['heat_treats'])
        result['total_profit'] = to_int(
            result['os_profit']) + to_int(result['pol_revenue'])
        result['client'] = queryset.first().client.name if queryset else Client.objects.filter(
            id=request.query_params['client']).first().name
        result['date'] = '{}-{}'.format(year, month)

        return Response(result)
