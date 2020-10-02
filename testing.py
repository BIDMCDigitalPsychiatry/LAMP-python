import LAMP 

def sensorResultsTest1():
    participant1 = "U7670518187"
    for p in LAMP.Participant.all_by_researcher("dc8jywy7rvcb0sm6b9wt")['data']:
        print(p['id'])
        LAMP.ParticipantExt(p['id'])
        break

        #print(len(LAMP.SensorEvent.all_by_participant(p['id'], origin='lamp.sms')['data']))
    #LAMP.ParticipantExt(participant1)
    #LAMP.ParticipantExt.sensor_results(participant=participant1)



if __name__ == "__main__":
    LAMP.connect() #credentials here
    
    #Test sensor results
    sensorResultsTest1()
