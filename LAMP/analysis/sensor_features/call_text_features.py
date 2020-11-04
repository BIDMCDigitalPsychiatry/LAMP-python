import datetime
import pandas as pd

def social_duration():
    """
    """
    pass

def conversational_degree():
    """
    """

    pass

def call_degree(data, times, resolution, label=1):
    """
    Find degree of call log (i.e. how many persons the user connected with over phone)
    """
    if 'lamp.calls' not in data:
        return None
    #Remove duplicate entries by converting call data to set
    call_data = set([(datetime.datetime.utcfromtimestamp(call[0] / 1000), tuple([(entry, call[1][entry]) for entry in call[1]])) for call in data['lamp.calls']])

    #Match each call with a corresponding time window
    callDf = pd.DataFrame([[min([t for t in times if t <= call[0]], key=lambda x: abs(x - call[0])), dict(call[1])['call_trace']] for call in call_data if dict(call[1])['call_type'] == label and call[0] >= sorted(times)[0] and call[0] <= sorted(times)[-1] + resolution], columns=['Date', 'Call Trace'])
    degreeDf = pd.DataFrame([[d, df.count().values[0]] for d, df in callDf.groupby('Date')], columns=['Date', 'Call Frequency'])
    return degreeDf

def call_duration(data, times, resolution, label=1):
    """
    Find call time

    :param
    :param
    :param label(int): indicates whether or not to query incoming calls (1) or outgoing calls (2)
    """
    if 'lamp.calls' not in data:
        return None
    #Remove duplicate entries by converting call data to set
    call_data = set([(datetime.datetime.utcfromtimestamp(call[0] / 1000), tuple([(entry, call[1][entry]) for entry in call[1]])) for call in data['lamp.calls']])

    #Match each call with a corresponding time window
    callDf = pd.DataFrame([[min([t for t in times if t <= call[0]], key=lambda x: abs(x - call[0])), dict(call[1])['call_duration']] for call in call_data if dict(call[1])['call_type'] == label and call[0] >= sorted(times)[0] and call[0] <= sorted(times)[-1] + resolution], columns=['Date', 'Call Duration'])
    durationDf = pd.DataFrame([[d, df['Call Duration'].sum()] for d, df in callDf.groupby('Date')], columns=['Date', 'Call Duration'])
    return durationDf

def call_number(data, times, resolution, label=1):
    """
    Find number of calls

    :param (str): 
    :param 
    :param label(int): indicates whether or not to query incoming calls (1), outgoing calls (2)
    """
    if 'lamp.calls' not in data:
        return None
        
    #Remove duplicate entries by converting call data to set
    call_data = set([(datetime.datetime.utcfromtimestamp(call[0] / 1000), tuple([(entry, call[1][entry]) for entry in call[1]])) for call in data['lamp.calls']])
    
    #Match each call with a corresponding time window
    print([call for call in call_data[1]])
    callDf = pd.DataFrame([[min([t for t in times if t <= call[0]], key=lambda x: abs(x - call[0])), call[1][1][1]] for call in call_data if dict(call[1])[1] == label and call[0] >= sorted(times)[0] and call[0] <= sorted(times)[-1] + resolution], columns=['Date', 'Call Type'])
    freqDf = pd.DataFrame([[d, df.count().values[0]] for d, df in callDf.groupby('Date')], columns=['Date', 'Call Frequency'])
    return freqDf
    
def all(sensor_data, dates, resolution):
    #print(sensor_data['lamp.calls'])
    incoming_calls, outgoing_calls = call_number(sensor_data, dates, resolution=resolution, label=1), call_number(sensor_data, dates, resolution=resolution, label=2)
    incoming_callduration, outgoing_callduration = call_duration(sensor_data, dates, resolution=resolution, label=1), call_duration(sensor_data, dates, resolution=resolution, label=2)

    df_list = [incoming_calls, outgoing_calls, incoming_callduration, outgoing_callduration]
    allDfs = reduce(lambda left, right: pd.merge(left, right, on=["Date"], how='left'), df_list)
    
    return allDfs
    
if __name__ == "__main__":
    pass
# def call_text_features(sensor_data, dates):
#     print('YO')
#     call_number(sensor_data, dates)
