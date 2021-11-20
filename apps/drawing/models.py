from django.db import models


class Drawing(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateField(default=None)
    is_closed = models.BooleanField(default=False)
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.SET_NULL,
        related_name='drawing',
        null=True
    )
    comment = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
