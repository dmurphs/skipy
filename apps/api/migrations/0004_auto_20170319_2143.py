# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170319_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Apr_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Aug_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Dec_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Feb_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Jan_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Jun_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Mar_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='May_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Nov_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Oct_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nrcs_monthlysnow',
            name='Sep_snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
