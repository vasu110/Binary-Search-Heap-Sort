# time = time.strftime("%H:%M")

import datetime

Alarm_Time = input("Enter time : ")
stop = False
print("On Process. Please Wait")

while stop == False:
    rn = str(datetime.datetime.now().time())
    if rn >= Alarm_Time:
        stop = True
        print("Alarm ON")