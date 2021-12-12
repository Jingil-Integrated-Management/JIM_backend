import django_filters

from .models import Drawing


class DrawingFilter(django_filters.FilterSet):

    created_at = django_filters.DateFilter(
        field_name='created_at', lookup_expr='exact')
    created_at__lte = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte')
    created_at__gte = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Drawing
        fields = ['client', 'name', 'is_closed', 'is_outsource']
