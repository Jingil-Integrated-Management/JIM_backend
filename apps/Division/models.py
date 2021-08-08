from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)

    main_division = models.IntegerField(blank=False, null=False)
    sub_division = models.IntegerField(blank=True, null=True)

    def __str__(self):
        sub_div = '-' + str(self.sub_division) if self.sub_division else ''
        return '{}{} / {}'.format(self.main_division, sub_div, self.name)

    def get_full_division(self):
        return self.__str__()
