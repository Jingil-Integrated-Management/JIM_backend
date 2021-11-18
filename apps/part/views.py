import os
from datetime import datetime

from django.core.files.storage import FileSystemStorage

from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from google.cloud import storage

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (OutSourceSerializer,
                          PartSerializer,
                          PartCreateSerializer)
from .models import Part, OutSource, File


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
    filterset_fields = ['division__main_division',
                        'division__sub_division', 'client']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PartSerializer
        else:
            return PartCreateSerializer

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
    serializer_class = PartSerializer


class PartFileCreateAPIView(CreateAPIView):
    queryset = File.objects.all()
    parser_classes = [MultiPartParser]

    def create(self, *args, **kwargs):
        file = self.request.data.get('file')
        file_type = file.name.split('.')[-1]
        file_name = 'file_{}.{}'.format(
            str(datetime.today().isoformat),
            file_type
        )
        if os.environ.get('DJANGO_SETTINGS_MODULE') == 'JIM.settings.dev_settings':
            fs = FileSystemStorage('uploads')
            created = File.objects.create(name=file_name, type=file_type)
            fs.save(file_name, file)
            return Response({'id': created.id, 'file': file_name})
        else:
            try:
                storage_client = storage.Client()
                bucket = storage_client.bucket('jim-storage')
                blob = bucket.blob(file_name)
                blob.upload_from_string(
                    file.file.read(), content_type='application/octet-stream')
                return Response('File {} uploaded'.format(file_name))

            except:
                return Response(
                    {'message': 'Cloud Storage Server Error'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
