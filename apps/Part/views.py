import os
from datetime import datetime

from django.core.files.storage import FileSystemStorage

from rest_framework.generics import (CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST as _400

from google.cloud import storage

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import OutSourceSerializer, PartListSerializer, PartSerializer
from .models import Part, OutSource, File


class OutSourceCreateAPIView(CreateAPIView):
    serializer_class = OutSourceSerializer
    queryset = OutSource.objects.all()


class PartListCreateAPIView(ListCreateAPIView):
    queryset = Part.objects.all().order_by('drawing__created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division__main_division',
                        'division__sub_division', 'client']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PartListSerializer
        else:
            return PartSerializer


class PartRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    lookup_url_kwarg = 'part_pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PartListSerializer
        else:
            return PartSerializer

class PartFileCreateAPIView(CreateAPIView):
    queryset = Part.objects.all()
    parser_classes = [MultiPartParser]

    def create(self, *args, **kwargs):
        file = self.request.data.get('file')
        if os.environ.get('DJANGO_SETTINGS_MODULE') == 'JIM.settings.dev_settings':
            fs = FileSystemStorage('uploads')
            file_name = ''.join(file.name.split('.')[:-1])
            file_type = file.name.split('.')[-1]
            file_name = '{}_{}.{}'.format(
                file_name,
                str(datetime.today()),
                file_type
            )
            created = File.objects.create(name=file_name, type=file_type)
            fs.save(file_name, file)
            return Response({'id': created.id, 'file': file_name})
        else:

            try:
                storage_client = storage.Client()
                bucket = storage_client.bucket('jingil-integrated-management')
                blob = bucket.blob(file.name)
                blob.upload_from_string(
                    file.file.read(), content_type='application/octet-stream')
                return Response('File {} uploaded'.format(file.name))

            except:
                return Response('Cloud Storage Server Error', _400)
