from django.db import models

import datetime


class Client(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, blank=True, null=True)
    contact = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class Drawing(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    created_at = models.DateField(default=datetime.date.today())
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='drawing')

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)

    main_division = models.IntegerField(blank=False, null=False)
    sub_division = models.IntegerField(blank=True, null=True)

    def __str__(self):
        sub_div = '-' + str(self.sub_division) if self.sub_division else ''
        return '{}{} / {}'.format(self.main_division, sub_div, self.name)


class Unit(models.Model):

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
