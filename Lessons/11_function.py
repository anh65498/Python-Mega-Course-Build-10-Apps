#function has 1 argument
def convert_minutes_to_hours(min):
    return min / 60;

#function has the second parameter as default parameter
#let default parameter be the last parameter
def convert_radius_to_area (radius, pi = 3.14):
    print(radius*radius* pi)

print(convert_minutes_to_hours(70) + 10);       #11.166666666666666
print(type(convert_minutes_to_hours(70)));      #<class 'float'>



#if only pass 1 argument, this function use default argument (3.14)
convert_radius_to_area(5);               #5*5*3.14 
#if pass 2 argument, this function use 6 instead of the default argument
convert_radius_to_area(5, 6);                   #5*5*6
