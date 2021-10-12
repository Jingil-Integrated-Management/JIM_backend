import datetime
from django.db import models

from apps.Client.models import Client


class Drawing(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateField(default=datetime.date.today)
    closed_at = models.DateField(default=None, null=True, blank=True)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, related_name='drawing', null=True)
    file_type = models.CharField(max_length=256, default='dwg')

    def __str__(self):
        return self.name

    def get_file(self):
        return self.name+'.'+self.file_type
