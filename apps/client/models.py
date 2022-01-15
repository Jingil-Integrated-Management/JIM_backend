from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=256)
    is_pinned = models.IntegerField(default=0)

    def __str__(self):
        return self.name
