import os
from datetime import datetime

from django.core.files.storage import FileSystemStorage

from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import (OutSourceSerializer,
                          PartReadSerializer,
                          PartWriteSerializer)
from .models import Part, OutSource, File
from .filters import PartFilter

from google.cloud import storage

from django_filters.rest_framework import DjangoFilterBackend


class OutSourceCreateAPIView(CreateAPIView):
    serializer_class = OutSourceSerializer
    queryset = OutSource.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'OutSource created.',
             'id': serializer.data['id']},
            status=status.HTTP_200_OK)


class OutSourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OutSource.objects.all()
    lookup_url_kwarg = 'outsource_pk'
    serializer_class = OutSourceSerializer


class PartListCreateAPIView(ListCreateAPIView):
    queryset = Part.objects.all().order_by('drawing__created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_class = PartFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PartWriteSerializer
        else:
            return PartReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'Part created.',
             'id': serializer.data['id']},
            status=status.HTTP_200_OK)


class PartRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    lookup_url_kwarg = 'part_pk'

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return PartWriteSerializer
        else:
            return PartReadSerializer


class PartFileCreateAPIView(CreateAPIView):
    queryset = File.objects.all()
    parser_classes = [MultiPartParser]

    def create(self, *args, **kwargs):
        file = self.request.data.get('file')
        file_type = file.name.split('.')[-1]
        file_name = 'file_{}.{}'.format(
            str(datetime.today().isoformat()),
            file_type
        )
        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket('jim-storage')
            blob = bucket.blob(file_name)
            blob.upload_from_string(
                file.file.read(), content_type='application/octet-stream')
        except:
            return Response(
                {'message': 'Cloud Storage Server Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        created = File.objects.create(name=file_name, type=file_type)
        return Response({'id': created.id, 'file': file_name})
