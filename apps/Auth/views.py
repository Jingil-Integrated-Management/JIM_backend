from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.status import HTTP_400_BAD_REQUEST as _400
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from .serializers import PasswordSerializer


class PasswordUpdateAPIView(UpdateAPIView):
    serializer_class = PasswordSerializer

    def get_object(self):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        old_password = serializer.data.get('old_password')
        new_password = serializer.data.get('new_password')
        if not user.check_password(old_password):
            return Response({'message': 'old_password is wrong'}, status=_400)
        if old_password == new_password:
            return Response({'message': 'choose a different password'}, status=_400)

        try:
            validate_password(new_password)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password updated successfully'})
        except ValidationError as error:
            return Response(error, status=_400)
