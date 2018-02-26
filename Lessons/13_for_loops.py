email_list = ["me@gmail.com", "you@yahoo.com", "they@gmail.com"]
names       = ["James", "John", "Kyle"]

#iterate a list
for item in email_list:
  print(item)

#iterate a list, if the string gmail is in the element, print it. If not, don't print
print ("emails in the list with @gmail")
for item in email_list:
    if "gmail" in item:
        print(item)

#Create a loop that iterates through the following list and prints out each item of the list in each iteration.
mylist = [1, 2, 3, 4, 5]
print("printing from 1 to 5: ")
for i in mylist:
    print(i)

#Loop through multiple lists at the same time
for i,j in zip(names, email_list):
    print(i, j)
