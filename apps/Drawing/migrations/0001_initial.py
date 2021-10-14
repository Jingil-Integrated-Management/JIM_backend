# Generated by Django 3.2.8 on 2021-10-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateField(default=None)),
                ('closed_at', models.DateField(blank=True, default=None, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawing', to='Client.client')),
                ('file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Drawing.file')),
            ],
        ),
    ]
