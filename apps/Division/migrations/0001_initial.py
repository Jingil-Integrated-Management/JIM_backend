# Generated by Django 3.2.8 on 2021-10-09 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_division', models.CharField(max_length=256)),
                ('sub_division', models.CharField(blank=True, max_length=256, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.client')),
            ],
        ),
    ]
