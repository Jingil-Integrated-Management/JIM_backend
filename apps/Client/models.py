from django.db import models


class Client(models.Model):
    business_id = models.CharField(max_length=256, unique=True)
    name = models.CharField(max_length=256)
    representative = models.CharField(max_length=256, null=True, blank=True)
    tel = models.CharField(max_length=128, null=True, blank=True)
    fax = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    note = models.TextField()
    manager = models.CharField(max_length=128, null=True, blank=True)
    manager_tel = models.CharField(max_length=128, null=True, blank=True)
    manager_phone = models.CharField(max_length=128, null=True, blank=True)
    primary_bank = models.CharField(max_length=128, null=True, blank=True)
    primary_bank_account = models.CharField(
        max_length=256, null=True, blank=True)
    bank_account_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name
