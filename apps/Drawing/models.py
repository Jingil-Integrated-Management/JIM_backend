import datetime
from django.db import models

from apps.Client.models import Client


class File(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Drawing(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateField(default=None)
    is_closed = models.BooleanField(default=False)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, related_name='drawing', null=True)
    file = models.OneToOneField(
        File, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_file(self):
        if self.file:
            return self.file.name
        else:
            return None
