import LAMP 
import datetime
import math
import pandas as pd

import altair as alt
from vega_datasets import data

"""
Helper functions for testing
"""
def date_list(results, resolution, days_cap=120):
    #Find the first, last date
    day_first = datetime.datetime.utcfromtimestamp(sorted([results[0][0]/1000 for dom in results])[0])
    day_last = datetime.datetime.utcfromtimestamp(sorted([results[-1][0]/1000 for dom in results])[-1])
    days_elapsed = (day_last - day_first).days 
    
    #Create based on resolution
    date_list = [day_first + (resolution * x) for x in range(0, math.ceil(min(days_elapsed, days_cap) * datetime.timedelta(days=1) / resolution))]

    #Create dateframe for the number of time units that have data; limited by days; cap at 'days_cap' if this number is large
    df = pd.DataFrame({'Date': date_list})
    return df

"""
TESTS
"""

"""
Participant creation tests
"""
def participantCreationTest1():
    participant1 = "U7670518187"
    subj = LAMP.ParticipantExt(participant1)
    print(subj.df)

"""
Main tests
"""
def sensorResultsTest1():
    participant1 = "U7670518187"
    for p in LAMP.Participant.all_by_researcher("dc8jywy7rvcb0sm6b9wt")['data']:
        print(p['id'])
        LAMP.ParticipantExt(p['id'])
        break

        #print(len(LAMP.SensorEvent.all_by_participant(p['id'], origin='lamp.sms')['data']))
    #LAMP.ParticipantExt(participant1)
    #LAMP.ParticipantExt.sensor_results(participant=participant1)


"""
Screen state tests
"""
def screenStateResultsTest1():
    test_part = "U7670518187"
    test_res = datetime.timedelta(days=1)
    partObj = LAMP.ParticipantExt(test_part)
    sensor_results = partObj.sensor_results()
    print(sensor_results.keys())
    df = date_list(sensor_results["lamp.screen_state"], test_res)

    LAMP.analysis.screen_features.charging_frequency(sensor_results, df)


"""
GPS
"""
def gpsTripTest(res, PART_ID='U7670518187'):
    '''
    res: (str) format is 'n'+min, where n is an integer
    '''
    part = LAMP.ParticipantExt(PART_ID)
    sensor_results = part.sensor_results()
    df = LAMP.analysis.sensor_features.gps_features.label_gps_points(sensor_results)

    l, df = LAMP.analysis.sensor_features.gps_features.get_trips(df)
    size = len(df)
    interval_range = pd.interval_range(df['timestamp'][0], df['timestamp'][size - 1], freq=res)
    trip_dict = LAMP.analysis.sensor_features.gps_features.gen_trip_dict(interval_range)
    trip_dict = LAMP.analysis.sensor_features.gps_features.get_trip_count(trip_dict, interval_range, l)
    print(trip_dict)

def gpsTripTestV1(df, res='30min'):
    '''
    res: (str) format is 'n'+min, where n is an integer
    '''
    # part = LAMP.ParticipantExt(PART_ID)cl
    # sensor_results = part.sensor_results()
    # df = label_gps_points(sensor_results)
    l, df = get_trips(df)
    size = len(df)
    interval_range = pd.interval_range(df['timestamp'][0], df['timestamp'][size - 1], freq=res)
    trip_dict = LAMP.analysis.screen_features.gps_features.gen_trip_dict(interval_range)
    trip_dict = LAMP.analysis.screen_features.gps_features.get_trip_count(trip_dict, l)
    print(trip_dict)


####
####

def stackedBarChartTest():
    """
    """
    #print(data.barley())
    test_part = "U7670518187"
    test_res = datetime.timedelta(days=1)
    partObj = LAMP.ParticipantExt(test_part)
    
    sliceObj = partObj.df#partObj.df.iloc[-10:]
    # print("HERE")
    sliceObj.loc[:, 'Date'] = sliceObj['Date'].apply(lambda x: x.date())
    sliceObj.loc[:, 'Sleep Duration'] = sliceObj['Sleep Duration'].apply(lambda x: x.hour + (x.minute / 60))
    sliceObj.loc[:, 'Active Duration'] = sliceObj['Active Duration'].apply(lambda x: x.hour + (x.minute / 60))
    sliceObj.loc[:, 'Sedentary Duration'] = sliceObj['Sedentary Duration'].apply(lambda x: x.hour + (x.minute / 60))


    # #print(partObj.df[['Date', 'Sleep Duration']])
    # # print(type(partObj.df.iloc[0]['Date']))#[['Date', 'Sleep Duration']])
    # # print(partObj.df.dtypes)
    graphDf = sliceObj[['Date', 'Sleep Duration', 'Active Duration', 'Sedentary Duration']].melt('Date', var_name='Measurement', value_name='Hours')
    graphDf.loc[:, 'Date'] = graphDf['Date'].astype(str)
    chart = alt.Chart(graphDf).mark_bar(size=20).encode(
        x=alt.X('Date:T', axis=alt.Axis(title='Date')),
        y=alt.Y('sum(Hours)', axis=alt.Axis(title='Hours')),

        # x='Date:T', 
        # y='sum(Hours)',
        color='Measurement'
    )

    chart.save("/home/ryan/activity_chart_test2.json")
    # sensor_results = partObj.sensor_results()
    # print(sensor_results.keys())
    # df = date_list(sensor_results["lamp.screen_state"], test_res)

    

    # source = data.barley()

    # chart = alt.Chart(source).mark_bar().encode(
    #     x='variety',
    #     y='sum(yield)',
    #     color='site')
    
    # chart.save("/home/ryan/vega_test.json")
    
if __name__ == "__main__":
    LAMP.connect() #REMOVE CREDENTIALS WHEN PUSHING
    participantCreationTest1()

    #Test sensor results

    #Main sensor results
    #sensorResultsTest1()

    #GPS Results
    #gpsTripTest(datetime.timedelta(days=1))
    #gpsTripTestV1(df, res=datetime.timedelta(days=1))

    #Screen State Results
    #screenStateResultsTest1()

    #Activity bar chart testing
    #stackedBarChartTest()