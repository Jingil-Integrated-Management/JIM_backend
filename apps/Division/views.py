from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED as _201,
    HTTP_400_BAD_REQUEST as _400)


from .serializers import DivisionSerializer
from .models import Division


class DivisionListCreateAPIView(ListCreateAPIView):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()
    pagination_class = None

    def get_queryset(self):
        query_param = self.request.query_params.get('client', None)
        if query_param:
            queryset = Division.objects.filter(
                unit__drawing__client=query_param)
        else:
            queryset = Division.objects.all()

        return queryset.distinct().order_by(
            'main_division', 'name', 'sub_division')

    def create(self, request, *args, **kwargs):

        obj = Division.objects.filter(
            name=request.data.get('name', None),
            main_division=request.data.get('main_division', None),
            sub_division=request.data.get('sub_division', None)
        )
        if obj:
            request.data['message'] = 'This division already exists!'
            return Response(request.data, status=_400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=_201, headers=headers)
