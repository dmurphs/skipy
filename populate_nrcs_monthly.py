import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skipy.settings')

import django
django.setup()

from csv import DictReader
from glob import glob

from apps.api.models import NRCS_MonthlySnow,NRCS_Locations

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def format_date(date_str,water_year):
    date_str = date_str.strip()
    if date_str == '' or date_str is None:
        return None
    else:
        date_components = date_str.split(' ')
        month_str = date_components[0]
        day_str = date_components[1]
        month_number = months.index(month_str) + 1
        month_num_str = str(month_number).zfill(2)

        new_date_str = '{year}-{month}-{day}'.format(year=water_year,month=month_num_str,day=day_str)
        return new_date_str

def create_record(row_dict,station):
    try:
        location = NRCS_Locations.objects.get(pk=station)
    except Exception as e:
        print e
        print station
        print row_dict
    monthly_snow_record = NRCS_MonthlySnow.objects.create(location=location,Water_Year=row_dict['Water_Year'])

    location.Station = station
    for field in row_dict:
        if 'collection_date' in field:
            row_dict[field] = format_date(row_dict[field],row_dict['Water_Year'])
        if row_dict[field] == '':
            row_dict[field] = None
        setattr(monthly_snow_record,field,row_dict[field])

    monthly_snow_record.save()

filenames = glob('../skipy_data/processed_snowmonth/*.csv')

for filename in filenames:
    with open(filename, 'r') as f:
        f_reader = DictReader(f)
        lines = [line for line in f_reader]

        file_basename = os.path.basename(filename)
        without_extension = file_basename.split('.')[0]
        station = without_extension.split('_')[-1]

        for row_dict in lines:
            create_record(row_dict,station)



    
    