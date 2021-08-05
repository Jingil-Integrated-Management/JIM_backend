from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, blank=True, null=True)
    contact = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name
