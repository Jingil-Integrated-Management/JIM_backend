import os

from rest_framework.generics import (
    CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST as _400
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from django.core.files.storage import FileSystemStorage

from .serializers import DrawingSerializer, DrawingRetreiveUpdateSerializer
from .models import Drawing


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
        uploads = os.listdir(os.path.relpath('./uploads'))
        if file.name in uploads:
            return Response(
                {'message': 'File {} exists'.format(file.name)}, status=_400)
        else:
            fs = FileSystemStorage('uploads')
            file_name = fs.save(file.name, file)
            return Response(file_name)
