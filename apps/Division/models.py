from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    code = models.CharField(max_length=256)

    def __str__(self):
        return '{} / {}'.format(self.name, self.code)

    def get_full_division(self):
        return self.__str__()
