# Generated by Django 3.2.6 on 2021-08-10 06:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawing', to='Client.client')),
            ],
        ),
    ]
