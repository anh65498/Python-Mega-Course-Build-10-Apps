#What is this? A script that block access to certain websites from a certain hour to a certain hour (Ex: 8am - 4pm)
#Learn: file manipulation, working with dates and times, run Python script in the background
'''How this work:
Host file contains the mappings of IP address to host names. Each entry should be kept on individual line. The IP address should be placed in the first column followed by the corresponding host name. The IP address and the host name should be separated by at least one space.
If you want to block Facebook, redirect the browser to the local IP address of your computer

 Example:
 127.0.0.1       localhost
 127.0.0.1       www.facebook.com

-> Run this Python script all the time in the background to check current time and Add/remove lines of text at certain times of the day to this host file

Assume the original "hosts" file does not contain the block websites
#For Mac user: use hosts_file_path_MAC and comment host_file_path_Window
#For Window user: use host_file_path_Window and comment hosts_file_path_Mac

This script is run in the background as soon as the computer starts

#HOW TO RUN THIS PROGRAM:
    In MacOs: Open Terminal: sudo python3 web_blocker.py
    In Window: Open cmd as administrator and open web_blocker.py
'''

import datetime
import time             #to delay the loop x seconds instead of running the loop every 1 milisec

hosts_file_path_Mac = "/private/etc/hosts"
host_file_path_Window= "C:\Windows\System32\drivers\etc"
#hosts_file_path = "hosts_test_file.txt"       #safety measurement - fake file
redirect_IP = "127.0.0.1"       #same for Window, Mac
websites_blocked_list = ["www.facebook.com", "facebook.com", "https://mangapark.com"]

#ask user for websites to block
print("***Enter websites to block. Enter 'done' when finish***")
while True:
    var = input("What websites do you want to block (Example: wwww.facebook.com): ")
    if var == "done":
        break
    else:
        websites_blocked_list.append(var)

#ask user for time to start blocking and unblocking websites
t_s = int(input("Time to start blocking (1-24): "))
t_e = int(input("Time to stop blocking (1-24): "))

time_start = datetime.time(t_s, 0, 0, 0)     #time start blocking (10am)
time_end   = datetime.time(t_e, 0, 0, 0)         #time stop blocking (8am)
#case 1: time_start < time_end, work_hour (done), fun_hour (done)
#case2: time_start > time_end, work_hour (done), fun_hour (done)

#open host file as a Python file object
file = open(hosts_file_path_Mac, 'r+')   #r+ for reading and writing
#file= open(hosts_test_file);                #for testing purposes. Accidentally Deleting hosts.txt of the system is annoying
content = file.readlines()
print(content)
print("Enter loop")

during_work_hour = False
removed_websites = False
added_websites = False
newcontent = ""
i = 0
#Loop that check the current time and block the websites
while True:
    #delay the loop every 30 seconds
    time.sleep(30)
    #check the current time
    time_now = datetime.datetime.now().time()

    if (time_start <= time_end):
        during_work_hour = (time_start <= time_now <= time_end)
    else:
        during_work_hour = (time_start <= time_now or time_now <= time_end)

    print("Work hour: %s" %during_work_hour)

    if (not(added_websites) and (during_work_hour)):
        print("Working hour. Blocking websites")
        #input("Break point")
        #add blocked websites list
        file.write("\n")
        for web in websites_blocked_list:
            file.write(redirect_IP + "\t" + web + "\n")
            print("add")
        added_websites = True
        file.close()           #file.write doesn't actually write until file is closed

    #FUN TIME
    if (not(during_work_hour)):
        print("Free time. Unblocking websites")
        file.seek(0)
        content = file.readlines()
        print("\t\tORIGINAL CONTENT: ")
        print(content)
        # input("Enter")

        #remove websites block by creating a new file without them
        if (not(removed_websites)):
            for line in content:
                print(line)
                for web in websites_blocked_list:
                    if web not in line:
                        newcontent += line
                        continue
                    else:
                        continue

            print("NEW CONTENT: %s" %newcontent)
            input("******** Enter:")
            print(newcontent)

            file2 = open(hosts_file_path_Mac, "w")
            file2.write(newcontent)

            file2.close()
            removed_websites = True
