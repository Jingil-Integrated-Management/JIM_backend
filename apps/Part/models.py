from django.db import models

from apps.Drawing.models import Drawing
from apps.Division.models import Division
from apps.Client.models import Client


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

    material_price = models.CharField(max_length=256, default=None, null=True)
    milling_price = models.CharField(max_length=256, default=None, null=True)
    heat_treat_price = models.CharField(
        max_length=256, default=None, null=True)
    wire_price = models.CharField(max_length=256, default=None, null=True)

    def __str__(self):
        return self.drawing.client.name + ' ' + str(self.division)
