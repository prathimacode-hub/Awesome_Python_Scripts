# From the USGS API: All earthquakes in PA or OR in the past 7 days

import requests
import datetime

endpoint = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
response = requests.get(endpoint)

status_code = response.status_code
if status_code == 200:
    quakes_list = response.json()['features']
    for quake_obj in quakes_list:
        place_str = quake_obj['properties']['place']
        if 'OR' in place_str or 'Oregon' in place_str or 'PA' in place_str or 'Pennsylvania' in place_str:
            print('Place: ' + str(quake_obj['properties']['place']))

            # Convert timestamp from "milliseconds since the epoch" to UTC
            sec = quake_obj['properties']['time'] / 1000.0
            date_time_str = datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S.%f')
            print('Date/time (UTC): ' + date_time_str)
            print('(subtract 5 hrs for PA, 8 hrs for OR)')

            print('Magnitude: ' + str(quake_obj['properties']['mag']))
            print('Type: ' + str(quake_obj['properties']['type']))
            if quake_obj['properties']['alert'] != None:
                print('Alert: ' + str(quake_obj['properties']['alert']))
            if quake_obj['properties']['tsunami'] > 0:
                print('Possible tsunami warning; see NOAA Tsunami website')
            if quake_obj['properties']['felt'] != None:
                print(str(quake_obj['properties']['felt']) + ' report(s) that it was felt')
            print('--------------------------------------------------')
    
else:
    print(f'Request was unsuccessful. Status code: {status_code}')
