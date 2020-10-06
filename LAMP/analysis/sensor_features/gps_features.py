import math 
import pandas as pd
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

def main(sensor_data, dates, resolution):
    labeled_data = label_gps_points(sensor_data)
    print(labeled_data)


if __name__ == "__main__":
    pass