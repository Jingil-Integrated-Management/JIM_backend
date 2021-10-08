from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, UserManager, PermissionsMixin)


class CustomUserManager(UserManager):

    def create_user(self, username, name, password=None):

        if not username:
            raise ValueError('Username field is missing!')

        user = self.model(username=username, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, name, password=None):
        superuser = self.model(username=username, name=name,
                               is_admin=True, is_staff=True, is_superuser=True)
        superuser.set_password(password)
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=32, unique=True, primary_key=True, null=False, blank=False)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username
