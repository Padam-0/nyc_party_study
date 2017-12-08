import pandas as pd

uber_names = ['pickup_datetime', 'pu_lat', 'pu_long', 'district']
yellow_names = ['pickup_datetime', 'dropoff_datetime' ,'pu_long',
                'pu_lat', 'do_long' ,'do_lat']
green_names = ['pickup_datetime', 'dropoff_datetime', 'pu_long',
               'pu_lat', 'do_long', 'do_lat']

"""
df = pd.read_csv('../data/small_uber.csv', names = uber_names,
                 index_col='pickup_datetime')
"""
df = pd.read_csv('../data/smallest_yellow.csv', names = yellow_names,
                 index_col='pickup_datetime')
"""
df = pd.read_csv('../data/smallest_green.csv', names = green_names,
                 index_col='pickup_datetime')
"""

with open('./smaller_yellow_data_pu.js', 'w') as file:
    file.write("function getPoints() {\n")
    file.write("return [\n")
    for i in range(len(df.index)):
        if i != len(df.index) - 1:
            file.write("new google.maps.LatLng({0}, {1}),\n".format(
                str(df.iloc[i]['pu_lat']), str(df.iloc[i]['pu_long'])))
        else:
            file.write("new google.maps.LatLng({0}, {1})".format(
                str(df.iloc[i]['pu_lat']), str(df.iloc[i]['pu_long'])))
    file.write("];\n}")