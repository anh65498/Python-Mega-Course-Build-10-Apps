# $alias python='python3'
# check out this helpful reference: https://pymotw.com/2/datetime/
import datetime         #module control date and time

#dir(datetime) in terminal will display all the functions in datetime modules
'''
['MAXYEAR', 'MINYEAR', '__doc__', '__file__', '__name__', '__pa
ckage__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedel
ta', 'tzinfo']
'''

#create a simple date object. Date class accepts three arguments: year, month, day
dob_object = datetime.date(1995, 12, 4)
print("My birthday is: %s" %dob_object)     #My birthday is: 1995-12-04


#get the datetime object, depending on the user's computer clock
time_now = (datetime.datetime.now())
print("The time now is: %s" %(time_now))      #date, time, minute,sec, microsec
print(type(time_now))

#subtract two moment of datetime
time_past = (datetime.datetime(2018, 2, 14, 20, 0, 0 ))
print("Time in the past: %s" %time_past)

print("time_now: %s" %time_now)         #same as time earlier when it was first assign because variable assignment
time_diff = time_now - time_past
print("Difference in time: %s" %(time_diff))
print(type(time_diff))          #datetime.timedelta


print("The total difference in day is: %s" %time_diff.days)
print("The total difference in seconds is: %s" %time_diff.seconds)

#timedelta
two_day_after = time_now + datetime.timedelta(days=2, minutes=5)
print (two_day_after)
