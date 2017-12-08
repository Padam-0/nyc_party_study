import pandas as pd

yellow_names = ['pickup_datetime', 'dropoff_datetime' ,'pu_long',
                'pu_lat', 'do_long' ,'do_lat']

df = pd.read_csv('../data/small_yellow.csv', names=yellow_names,
                 parse_dates=True)

print(df.head())

print(df['dropoff_datetime'] - df['pickup_datetime'])

for i in range(1000):
    print(pd.to_datetime(str(df['dropoff_datetime'])) - pd.to_datetime(str(df[
                                                                      'pickup_datetime'])))