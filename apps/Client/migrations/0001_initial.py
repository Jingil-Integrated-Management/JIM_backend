# Generated by Django 3.2.8 on 2021-10-18 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.CharField(max_length=256, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('representative', models.CharField(blank=True, max_length=256, null=True)),
                ('tel', models.CharField(blank=True, max_length=128, null=True)),
                ('fax', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('manager', models.CharField(blank=True, max_length=128, null=True)),
                ('manager_tel', models.CharField(blank=True, max_length=128, null=True)),
                ('manager_phone', models.CharField(blank=True, max_length=128, null=True)),
                ('primary_bank', models.CharField(blank=True, max_length=128, null=True)),
                ('primary_bank_account', models.CharField(blank=True, max_length=256, null=True)),
                ('bank_account_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
