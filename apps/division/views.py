from django.db.models import query
from django.db.models.query_utils import Q
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DivisionSerializer, MainDivisionSerializer
from .models import Division


class DivisionListCreateAPIView(ListCreateAPIView):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client', 'main_division', 'sub_division']
    pagination_class = None

    def get_queryset(self):
        query_param = self.request.query_params.get('client', None)
        if query_param:
            queryset = Division.objects.filter(client=query_param)
        else:
            queryset = Division.objects.all()

        return queryset.distinct().order_by('main_division', 'sub_division')

    def create(self, request, *args, **kwargs):

        obj = Division.objects.filter(
            main_division=request.data.get('main_division', None))
        sub_division = request.data.get('sub_division', None)

        if not sub_division:
            obj = obj.filter(sub_division__isnull=True)
        else:
            obj = obj.filter(sub_division=sub_division)

        if obj:
            request.data['message'] = 'This division already exists!'
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers)


class DivisionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_url_kwarg = 'division_pk'

    def update(self, request, *args, **kwargs):

        main_division = self.request.data.get('main_division', None)
        sub_division = self.request.data.get('sub_division', None)
        client = self.request.data.get('client', None)

        instance = self.get_object()
        queryset = Division.objects.all()

        if main_division:
            queryset = queryset.filter(main_division=main_division)
        else:
            queryset = queryset.filter(main_division=instance.main_division)
        if sub_division:
            queryset = queryset.filter(sub_division=sub_division)
        else:
            queryset = queryset.filter(sub_division=instance.sub_division)
        if client:
            queryset = queryset.filter(client=client)
        else:
            queryset = queryset.filter(client=instance.client)

        if queryset:
            request.data['message'] = 'This division already exists!'
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)


class MainDivisionListAPIView(ListAPIView):
    queryset = Division.objects.all().values('main_division').distinct()
    pagination_class = None
    serializer_class = MainDivisionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']
