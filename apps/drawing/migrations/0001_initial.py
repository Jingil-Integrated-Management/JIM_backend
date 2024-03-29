# Generated by Django 3.2.8 on 2021-12-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateField(default=None)),
                ('is_closed', models.BooleanField(default=False)),
                ('is_outsource', models.BooleanField()),
                ('comment', models.TextField(blank=True, default=None, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drawings', to='client.client')),
            ],
        ),
    ]
