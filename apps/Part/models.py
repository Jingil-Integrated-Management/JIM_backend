from django.db import models

from apps.Drawing.models import Drawing
from apps.Division.models import Division
from apps.Client.models import Client


class File(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Material (models.Model):
    name = models.CharField(max_length=128, primary_key=True)


class OutSource(models.Model):

    material_price = models.CharField(
        max_length=256, default=None, null=True, blank=True)
    milling_price = models.CharField(
        max_length=256, default=None, null=True, blank=True)
    heat_treat_price = models.CharField(
        max_length=256, default=None, null=True, blank=True)
    wire_price = models.CharField(
        max_length=256, default=None, null=True, blank=True)

    material_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='material_clients',
        null=True, blank=True)
    milling_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='milling_clients',
        null=True, blank=True)
    heat_treat_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='heat_treat_clients',
        null=True, blank=True)
    wire_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='wire_clients',
        null=True, blank=True)

    def __str__(self):
        return self.part.__str__()


class Part(models.Model):
    drawing = models.ForeignKey(
        Drawing, on_delete=models.CASCADE, related_name='parts', db_index=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    outsource = models.OneToOneField(
        OutSource,
        related_name='part',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    file = models.OneToOneField(
        File, on_delete=models.CASCADE, null=True, blank=True)

    x = models.CharField(max_length=256)
    y = models.CharField(max_length=256)
    z = models.CharField(max_length=256)
    quantity = models.IntegerField(default=1)

    price = models.CharField(max_length=256)
    comment = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.drawing.client.name + ' ' + str(self.division)

    def get_file(self):
        if self.file:
            return self.file.name
        else:
            return None
