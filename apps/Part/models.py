from django.db import models

from apps.Drawing.models import Drawing
from apps.Division.models import Division


class Part(models.Model):

    MATERIAL_CHOICES = [
        ('SKS3', 'SKS3'),
        ('SKD61', 'SKD61'),
        ('KP1', 'KP1'),
    ]

    drawing = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    x = models.CharField(max_length=256)
    y = models.CharField(max_length=256)
    z = models.CharField(max_length=256)

    price = models.CharField(max_length=256)
    material = models.CharField(
        max_length=256, choices=MATERIAL_CHOICES, default='SKS3')

    comment = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.drawing.client.name + ' ' + str(self.division)
