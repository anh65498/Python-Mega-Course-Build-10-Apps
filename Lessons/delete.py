import datetime
import time             #module to control the time

time_now = (datetime.datetime.now())       #date, time, minute,sec, microsec
print("Time now: %s" %time_now)
print(type(time_now))

time_past = (datetime.datetime(2018, 2, 14, 20, 0, 0 ))
print("Time in the past: %s" %time_past)

print("time_now: %s" %time_now)         #same as time earlier when it was first assign because variable assignment
time_diff = time_now - time_past
print("Difference in time: %s" %(time_diff))
print(type(time_diff))          #datetime.timedelta
