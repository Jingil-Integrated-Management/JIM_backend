import os
from datetime import datetime

from rest_framework.generics import (
    CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST as _400
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from django.core.files.storage import FileSystemStorage

from google.cloud import storage

from .serializers import DrawingSerializer, DrawingRetreiveUpdateSerializer
from .models import Drawing, File


class DrawingListCreateAPIView(ListCreateAPIView):
    serializer_class = DrawingSerializer
    queryset = Drawing.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'client']
    search_fields = ['name', 'client__name']


class DrawingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DrawingRetreiveUpdateSerializer
    queryset = Drawing.objects.all()
    lookup_url_kwarg = 'drawing_pk'


class DrawingFileCreateAPIView(CreateAPIView):
    queryset = Drawing.objects.all()
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
                response = blob.upload_from_string(
                    file.file.read(), content_type='application/octet-stream')
                return Response('File {} uploaded'.format(file.name))

            except:
                return Response('Cloud Storage Server Error', _400)
