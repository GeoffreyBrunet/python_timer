import os
import datetime
import time
 
os.system('clear')
 
getTime = input("Temps pour déclencher le minuteur ? ")

parseTime = getTime.split(':')

getSeconds = int(parseTime[0])*3600

getMins = int(parseTime[1])*60

getHour = int(parseTime[2])

getCount = int(parseTime[0])*3600 + int(parseTime[0])*60 + int(parseTime[2])

intTime = datetime.datetime.now()

endTime = intTime + datetime.timedelta(seconds=getCount)
 
while(1):
    os.system('clear')
    delta = endTime - datetime.datetime.now()
    print("hours: "+ str(getHour) + " mins: " + str(getMins) + " seconds: " + str(delta.seconds))
    if (delta.seconds <= 0):
        print("TEMPS ÉCOULÉ !\n")
        break
    time.sleep(1)