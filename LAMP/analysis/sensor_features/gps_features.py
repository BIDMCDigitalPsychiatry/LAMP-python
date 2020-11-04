import math 
import pandas as pd
import numpy as np
from datetime import datetime
from geopy import distance

def label_gps_points(sensor_data):
    """
    Label gps readings as being either "stationary" (0) or "transitionary" (1)

    :param sensor_data (dict): maps LAMP sensor to sensor events
    
    :return (pd.DataFrame): columns ['timestamp', 'latitude', 'longitude', 'stationary'], where 'stationary' is bool indicating whether GPS point is stationary/nonstationary
    """
    SPEED_THRESHOLD = 1.0

    labeled_data = []
    for point1, point2 in zip(sensor_data['lamp.gps'], sensor_data['lamp.gps'][1:]):
        dist = distance.distance((point1[1]['latitude'], point1[1]['longitude']), (point2[1]['latitude'], point2[1]['longitude'])).km 
        speed =  dist / ((datetime.utcfromtimestamp(point2[0] / 1000) - datetime.utcfromtimestamp(point1[0] / 1000)).seconds / 3600)
        
        if speed >= SPEED_THRESHOLD: stationary = False
        else: stationary = True
        
        labeled_data.append([point1[0], point1[1]['latitude'], point1[1]['longitude'], stationary])
        
    #Take car of last point by just adding label as 
    last_point = sensor_data['lamp.gps'][-1]
    labeled_data.append([last_point[0], last_point[1]['latitude'], last_point[1]['longitude'], labeled_data[-1][-1]])
    return pd.DataFrame(labeled_data, columns=['timestamp', 'latitude', 'longitude', 'stationary'])


def get_trips(df, state=False, inclusive=True):
    '''
    Input:
    df (Pandas Dataframe)
    state (bool)
    inclusive (bool)

    Returns: list of trips (tuples of start and end timestamps)
    '''
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    arr = np.array(df['stationary'])
    arr_ext = np.r_[False, arr == state, False]
    #print(arr_ext[:-1])
    idx = np.flatnonzero(arr_ext[:-1] != arr_ext[1:])
    idx_list = list(zip(idx[:-1:2], idx[1::2] - int(inclusive)))
    #print(arr_ext, idx, idx[1::2])
    trip_list = []
    for tup in idx_list:
        trip = (df['timestamp'][tup[0]], df['timestamp'][tup[1]],)
        trip_list.append(trip)
    return trip_list, df

def gen_trip_dict(interval_range):
    trip_dict = {}
    for i in range(len(interval_range)):
        trip_dict[interval_range[i]] = {'Trip Count': 0, 'Duration': 0, 'Distance Traveled': 0}
    return trip_dict

def get_trip_count(trip_dict, interval_range, l):
    for i in range(len(interval_range)):
        for j in range(len(l)):
            if l[j][0] >= interval_range[i].left and l[j][1] <= interval_range[i].right:
                trip_dict[interval_range[i]]['Trip Count'] += 1
    return trip_dict


def uploadMarkers():
    pass


def all(sensor_data, dates, resolution):
    labeled_data = label_gps_points(sensor_data)
    print(get_trips(labeled_data))


if __name__ == "__main__":
    pass