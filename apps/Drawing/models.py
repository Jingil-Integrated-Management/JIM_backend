import datetime

from django.db import models

from apps.Client.models import Client


class Drawing(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    created_at = models.DateField(default=datetime.date.today())
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='drawing')

    def __str__(self):
        return self.name
