# Generated by Django 3.2.6 on 2021-08-20 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
        ('Division', '0001_initial'),
        ('Drawing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=256)),
                ('y', models.CharField(max_length=256)),
                ('z', models.CharField(max_length=256)),
                ('price', models.CharField(max_length=256)),
                ('material', models.CharField(choices=[('SKS3', 'SKS3'), ('KP4', 'KP4'), ('SKD61', 'SKD61')], default='SKS3', max_length=256)),
                ('comment', models.TextField(blank=True, default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.client')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Division.division')),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='Drawing.drawing')),
            ],
        ),
        migrations.CreateModel(
            name='OS_Part',
            fields=[
                ('part_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Part.part')),
                ('material_price', models.CharField(max_length=256)),
                ('milling_price', models.CharField(max_length=256)),
                ('heat_treat_price', models.CharField(max_length=256)),
            ],
            bases=('Part.part',),
        ),
    ]
