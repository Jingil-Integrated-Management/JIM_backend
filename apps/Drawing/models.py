from django.db import models

from apps.Client.models import Client


class Drawing(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateField(default=None)
    is_closed = models.BooleanField(default=False)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, related_name='drawing', null=True)

    def __str__(self):
        return self.name
