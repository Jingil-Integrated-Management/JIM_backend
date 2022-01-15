from django.contrib.auth.password_validation import validate_password

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.exceptions import ValidationError

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

        old_password = serializer.data['old_password']
        new_password = serializer.data['new_password']

        if not user.check_password(old_password):
            raise ValidationError({'message': 'old_password is wrong'})
        if old_password == new_password:
            raise ValidationError({'message': 'choose a different password'})

        validate_password(new_password)
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password updated successfully'})
