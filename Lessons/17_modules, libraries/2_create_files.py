#create 2 text files that has the current time and date as the file name
import datetime


#function definition: create a file with filename as the file's name
def create_file_date_and_time():
    filename = datetime.datetime.now();   # same as datetime.datetime.today()
    print (str(filename))
    with open(str(filename) + ".txt" ,"w") as file:       #filename is of type datetime --> string, ".txt" to create a text file
        pass;       #not really writing anything in the file

#call function
print ("create a file whose name is date and time at the moment of creation")
create_file_date_and_time();


#formating characters: instead of ":", use "-"
#to format the string of datetime object, use strftime.
# strftime method creates a string that rep the time in a more human readable format
#Go to http://strftime.org for referece

print()
def create_file_date():
    filename = datetime.datetime.now()
    filename = filename.strftime("%A %m %d %Y")
    print(str(filename))
    with open(str(filename) + ".txt","w") as file:       #filename is of type datetime --> string
        pass;       #not really writing anything in the file

print ("create a file whose name is the date at the moment of creation")
create_file_date();
