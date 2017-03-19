# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NRCS_Locations',
            fields=[
                ('Site_Name', models.CharField(max_length=100)),
                ('Station', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Ntwk', models.CharField(max_length=5)),
                ('Elev', models.IntegerField()),
                ('Lat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Lon', models.DecimalField(decimal_places=2, max_digits=6)),
                ('installed', models.PositiveSmallIntegerField()),
                ('state', models.CharField(max_length=2)),
                ('County', models.CharField(max_length=100)),
                ('Hydrologic_Unit', models.CharField(max_length=255)),
                ('SHEF', models.CharField(max_length=7)),
            ],
        ),
    ]