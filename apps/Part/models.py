from django.db import models

from apps.Drawing.models import Drawing
from apps.Division.models import Division
from apps.Client.models import Client

from model_utils.managers import InheritanceManager


class Part(models.Model):

    MATERIAL_CHOICES = [
        ('SKS3', 'SKS3'),
        ('KP4', 'KP4'),
        ('SKD61', 'SKD61')
    ]

    drawing = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name='parts')
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    x = models.CharField(max_length=256)
    y = models.CharField(max_length=256)
    z = models.CharField(max_length=256)

    price = models.CharField(max_length=256)
    material = models.CharField(
        max_length=256, choices=MATERIAL_CHOICES, default='SKS3')

    comment = models.TextField(default=None, null=True, blank=True)

    objects = InheritanceManager()

    def __str__(self):
        return self.drawing.client.name + ' ' + str(self.division)


class OS_Part(Part):
    material_price = models.CharField(max_length=256)
    milling_price = models.CharField(max_length=256)
    heat_treat_price = models.CharField(max_length=256)
    wire_price = models.CharField(max_length=256)
