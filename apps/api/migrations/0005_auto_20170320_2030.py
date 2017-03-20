# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170319_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='County',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Elev',
            new_name='elev',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Hydrologic_Unit',
            new_name='hydrologic_unit',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Lon',
            new_name='lon',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Ntwk',
            new_name='ntwk',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='SHEF',
            new_name='shef',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Site_Name',
            new_name='site_name',
        ),
        migrations.RenameField(
            model_name='nrcs_locations',
            old_name='Station',
            new_name='station',
        ),
        migrations.RenameField(
            model_name='nrcs_monthlysnow',
            old_name='Water_Year',
            new_name='water_year',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Apr_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Apr_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Apr_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Aug_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Aug_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Aug_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Dec_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Dec_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Dec_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Feb_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Feb_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Feb_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jan_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jan_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jan_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jul_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jul_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jul_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jun_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jun_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Jun_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Mar_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Mar_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Mar_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='May_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='May_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='May_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Nov_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Nov_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Nov_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Oct_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Oct_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Oct_snow_water_equivalent',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Sep_collection_date',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Sep_snow_depth',
        ),
        migrations.RemoveField(
            model_name='nrcs_monthlysnow',
            name='Sep_snow_water_equivalent',
        ),
        migrations.AddField(
            model_name='nrcs_monthlysnow',
            name='collection_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='nrcs_monthlysnow',
            name='collection_month',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nrcs_monthlysnow',
            name='snow_depth',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nrcs_monthlysnow',
            name='snow_water_equivalent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
