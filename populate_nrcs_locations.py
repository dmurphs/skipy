import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skipy.settings')

import django
django.setup()

from csv import reader

from apps.api.models import NRCS_Locations

def create_record(ld):
    location = NRCS_Locations.objects.create(
        Site_Name=ld[0],
        Station=ld[1],
        Ntwk=ld[2],
        Elev=ld[3],
        Lat=ld[4],
        Lon=ld[5],
        installed=ld[6],
        state=ld[7],
        County=ld[8],
        Hydrologic_Unit=ld[9],
        SHEF=ld[10]
    )

    location.save()

with open('../skipy_data/location_metadata.csv', 'r') as f:
    location_metadata = list(reader(f))[1:]
    for location in location_metadata:
        create_record(location)

    