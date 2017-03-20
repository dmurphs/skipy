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

def field_prefix(field_name):
    return field_name.split('_')[0]

def is_null_or_empty(text):
    return text == '' or text == None

def remove_empty_fields(row_dict):
    return {field: row_dict[field] for field in row_dict if not is_null_or_empty(row_dict[field])}

def remove_prefix(field_name):
    components = field_name.split('_')
    return '_'.join(components[1:])

def get_months_data(row_dict):
    row_data = remove_empty_fields(row_dict)
    field_prefixes = [field_prefix(field) for field in row_data]
    included_months = [month for month in months if month in field_prefixes]

    months_data = {}

    for month in included_months:
        month_num = months.index(month) + 1
        month_fields = [field for field in row_data if field_prefix(field) == month]
        month_data = {remove_prefix(field): row_data[field] for field in month_fields}
        months_data[month_num] = month_data

    return months_data

def create_record(month_num,month_data,station,water_year):
    location = NRCS_Locations.objects.get(pk=station)
    monthly_snow_record = NRCS_MonthlySnow.objects.create(location=location,water_year=water_year,collection_month=month_num)

    for field in month_data:
        if field == 'collection_date':
            month_data[field] = format_date(month_data[field],water_year)
        if month_data[field] == '':
            month_data[field] = None
        setattr(monthly_snow_record,field,month_data[field])

    monthly_snow_record.save()

def split_csv_row_into_records(row_dict,station):
    months_data = get_months_data(row_dict)
    for month_num in months_data:
        month_data = months_data[month_num]
        water_year = row_dict['Water_Year']
        create_record(month_num,month_data,station,water_year)

filenames = glob('../skipy_data/processed_snowmonth/*.csv')

for filename in filenames:
    with open(filename, 'r') as f:
        f_reader = DictReader(f)
        lines = [line for line in f_reader]

        file_basename = os.path.basename(filename)
        without_extension = file_basename.split('.')[0]
        station = without_extension.split('_')[-1]

        for row_dict in lines:
            split_csv_row_into_records(row_dict, station)



    
    