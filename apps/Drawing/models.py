import datetime
from django.db import models

from apps.Client.models import Client


class Drawing(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    created_at = models.DateField(default=datetime.date.today)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, related_name='drawing', null=True)
    file_type = models.CharField(max_length=256, default='dwg')

    def __str__(self):
        return self.name

    def get_file(self):
        return self.name+'.'+self.file_type
