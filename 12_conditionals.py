#Excercise 1
# a = 5
#
# if a < 5:
#     print ("Less than 5")
# elif a == 5:
#     print("equal to 5")
# else:
#     print("greater than 5")


#########################
#Exercise 2
def add_50(age):
    return age + 50;

age = input("what's your age? ")
age = int(age);                 #or age = int(input("what's your age? "))

if (age <= 150):
    print("You age in 50 years: %d" %(add_50(age)))
else:
    print("Your age is unrealistic")


#########################
#Exercise 3
#print out the string length but not if the argument is an int or float
def string_length(mystring):
    if (type(mystring) == int):
        print("error. Do not pass integers")
    elif (type(mystring) == float):
        print("error. Do not pass float numbers")
    else:
        print(len(mystring))

string_length("hello world")
string_length(453)
string_length(-4.5)


########################
#Exercise 4
#convert Celsius degree to Fahrenheit
def cel_to_fahr(cel):
    if (cel < -273.15):
        print("Invalid celsius degree. Physical matter can reach -273.15 C")
    else:
        fah = cel * 9/5 + 32;
        return fah;

cel_to_fahr
