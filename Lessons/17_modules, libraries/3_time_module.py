#time module: good for delaying actions
import time
import datetime

time_now    = datetime.datetime.now()
two_day_after = time_now + datetime.timedelta(days=2, minutes=5)
print (two_day_after)

#create a list which each datetime object is 1 day and 10 mins apart
list = []
var        = time_now;
#for each loop, add a time object that is 3 more days and 10 min more than the previous
print ("Loops of datetime object that are 3 more days and 10 min apart:")
for i in range(0,5):
     list.append(var);          #lst[i] = time    will cause error because lst originally is ampty
     var = list[i] + datetime.timedelta(days=3, minutes=10)
     print (list[i])


#now, create a loop that will add 7 datetime object which are 8 minutes apart
new_list = []
#time object that is 3 more days and 10 min more than the previous
print("Loops of datetime objects that are 3 seconds apart from my birthday. Don't want to wait too long
for index in range(0,7):
    new_list.append(datetime.datetime.now())
    time.sleep(3)        #argument is in second(s)
    print(new_list[index])
