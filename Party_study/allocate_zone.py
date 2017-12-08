import subprocess
from heapq import heappush, heappop
import sys
import pandas as pd
import matplotlib.path as mplPath
import numpy as np

def test_point(lat, long, zones):

    heap = []

    for zone, points in zones.items():
        centroid_lat = np.mean([i[0][1] for i in points])
        centroid_long = np.mean([i[0][0] for i in points])

        a = centroid_lat - lat
        b = centroid_long - long

        distance = np.sqrt((a ** 2) + (b ** 2))
        heappush(heap, (distance, zone))

    for i in range(len(zones)):
        closest_zone = heappop(heap)

        path = []
        for i in range(len(zones[closest_zone[1]])):
            path.extend(zones[closest_zone[1]][i])
        path.extend(zones[closest_zone[1]][0])

        path = np.array(path)

        bbPath = mplPath.Path(path)

        if bbPath.contains_point(([long, lat])) == 1:
            return closest_zone[1]

    return "XX00"

def main():

    stream = int(sys.argv[1])

    yellow_names = ['pickup_datetime', 'dropoff_datetime' ,'pu_long',
                    'pu_lat', 'do_long' ,'do_lat']

    df = pd.read_csv('./geographic.csv')


    yellow_cabs = pd.read_csv('./clean_yellow.csv', names =
                             yellow_names, index_col='pickup_datetime')

    if stream == 1:
        stop = 3387532

        output_filename = "./zone_data.csv"

        a = subprocess.Popen(['wc', '-l', output_filename], stdout=subprocess.PIPE)
        wc = int(a.communicate()[0].rstrip().decode().split(' ')[0])
        start = 0 + wc
    else:
        stop = 6775065
        output_filename = "./zone_data_1.csv"

        a = subprocess.Popen(['wc', '-l', output_filename], stdout=subprocess.PIPE)
        wc = int(a.communicate()[0].rstrip().decode().split(' ')[0])
        start = 3387532 + wc

    """
    zd = pd.read_csv('./zone_data.csv', names=['pu_dt', 'pu_zone', 'do_zone'],
                     index_col='pu_dt')

    result = pd.concat([yellow_cabs, zd], axis=1, join_axes=[yellow_cabs.index])

    result.to_csv("final_zone_df.csv")
    """
    zones = {}

    for i, nbrhood in enumerate(df):
        boundary = df[nbrhood].as_matrix().reshape(int(df[nbrhood].size / 2),2)
        boundary = boundary[~np.isnan(boundary)]
        bd = []
        for j in range(int(len(boundary) / 2)):
            k = [[boundary[j*2], boundary[j*2 + 1]]]
            bd.append(k)
        zones[nbrhood] = bd

    for row in range(start, stop):
        pu_lat, pu_long = yellow_cabs.ix[row,:].values[2], yellow_cabs.ix[row,
                                                          :].values[1]
        do_lat, do_long = yellow_cabs.ix[row, :].values[4], yellow_cabs.ix[row,
                                                           :].values[3]
        ind = yellow_cabs.index[row]
        with open(output_filename, "a") as file:
            file.write(ind + ',' + test_point(pu_lat, pu_long, zones) + ','
                       + test_point(do_lat, do_long, zones) + '\n')

if __name__ == '__main__':
    main()
