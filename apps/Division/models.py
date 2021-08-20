from django.db import models

from apps.Client.models import Client


class Division(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    code = models.CharField(max_length=256)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return '{} / {}'.format(self.name, self.code)

    def get_full_division(self):
        return self.__str__()
