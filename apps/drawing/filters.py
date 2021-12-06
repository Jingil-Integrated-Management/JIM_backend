import django_filters

from .models import Drawing


class DrawingFilter(django_filters.FilterSet):

    created_at = django_filters.DateFilter(
        field_name='created_at', lookup_expr='exact')
    created_at__lte = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte')
    created_at__gte = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte')
    outsource_isnull = django_filters.BooleanFilter(
        field_name='parts__outsource', lookup_expr='isnull')

    class Meta:
        model = Drawing
        fields = ['client', 'name', 'is_closed']
