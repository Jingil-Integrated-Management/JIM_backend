from django.db import models

from apps.Client.models import Client


class Division(models.Model):
    main_division = models.CharField(max_length=256, blank=False, null=False)
    sub_division = models.CharField(max_length=256, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        sub_div = '/ ' + str(self.sub_division) if self.sub_division else ''
        return '{}{}'.format(self.main_division, sub_div)

    def get_full_division(self):
        return self.__str__()
