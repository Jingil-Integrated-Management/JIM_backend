# Generated by Django 3.2.8 on 2021-12-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('division', '0001_initial'),
        ('drawing', '0001_initial'),
        ('client', '0001_initial'),
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
            name='Material',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OutSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_price', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('milling_price', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('heat_treat_price', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('wire_price', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('heat_treat_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='heat_treat_clients', to='client.client')),
                ('material_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_clients', to='client.client')),
                ('milling_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milling_clients', to='client.client')),
                ('wire_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wire_clients', to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=256)),
                ('y', models.CharField(max_length=256)),
                ('z', models.CharField(max_length=256)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.CharField(max_length=256)),
                ('comment', models.TextField(blank=True, default=None, null=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='division.division')),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='drawing.drawing')),
                ('file', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part.file')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part.material')),
                ('outsource', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part', to='part.outsource')),
            ],
        ),
    ]
