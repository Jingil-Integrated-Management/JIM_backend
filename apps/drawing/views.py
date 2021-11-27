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

from apps.part.models import Part

from .serializers import DrawingReadSerializer, DrawingWriteSerializer
from .models import Drawing
from .filters import DrawingFilter

from utils.utils import to_int


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

        result = [
            {
                'client': client,
                'drawings': list(drawings)
            } for client, drawings in data
        ]
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


class StatisticsAPIView(APIView):
    pagination_class = None

    def get(self, request):
        year, month = request.query_params['date'].split('-')
        queryset = Drawing.objects.filter(client=request.query_params['client']).filter(
            created_at__gte='{}-{}-{}'.format(year, month, '01'),
            created_at__lte='{}-{}-{}'.format(year, month,
                                              calendar.monthrange(int(year), int(month))[1])
        ).prefetch_related('parts')

        os_info = Part.objects.exclude(outsource=None).filter(drawing__in=queryset).aggregate(
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

        pol_info = Part.objects.filter(outsource=None).filter(drawing__in=queryset).aggregate(
            pol_revenue=Sum(
                Cast(F('price'), output_field=IntegerField()) * F('quantity')),
        )

        result = {**os_info, **pol_info}
        result['total_revenue'] = to_int(
            result['os_revenue']) + to_int(result['pol_revenue'])
        result['os_profit'] = to_int(result['os_revenue']) \
            - to_int(result['materials']) \
            - to_int(result['millings']) \
            - to_int(result['wires']) \
            - to_int(result['heat_treats'])
        result['total_profit'] = to_int(
            result['os_profit']) + to_int(result['pol_revenue'])

        result['client'] = queryset.first().client.name
        result['date'] = '{}-{}'.format(year, month)

        return Response(result)
