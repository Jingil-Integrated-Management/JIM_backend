from django.db.models import fields
import django_filters

from .models import Part


class PartFilter(django_filters.FilterSet):

    main_division = django_filters.CharFilter(
        field_name='division', lookup_expr='main_division')
    sub_division = django_filters.CharFilter(
        field_name='division', lookup_expr='sub_division')
    created_at = django_filters.DateFilter(
        field_name='drawing', lookup_expr='created_at')
    created_at__lte = django_filters.DateFilter(
        field_name='drawing', lookup_expr='created_at__lte')
    created_at__gte = django_filters.DateFilter(
        field_name='drawing', lookup_expr='created_at__gte')
    client = django_filters.NumberFilter(
        field_name='drawing', lookup_expr='client')
    is_outsource = django_filters.BooleanFilter(
        field_name='drawing', lookup_expr='is_outsource')
    is_closed = django_filters.BooleanFilter(
        field_name='drawing', lookup_expr='is_closed')

    class Meta:
        model = Part
        fields = '__all__'
