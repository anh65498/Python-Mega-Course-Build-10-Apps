#create a list
list = [1,2,"Hello"]

#create a dictionary
dict = {
    "name": "Anh Pham",
    "surname": "N.P",
    "age":  22,
    "major": "computer science",
    "cities": ("Saigon", "San Jose", "Los Angeles")     #a tuple
}

#accesing a value in dictionary, don't need to know index but need key
print("surname is " + dict["surname"])
print(("age is %d")    %dict["age"])
#print("have lived in %s"    %dict["cities"])       #can't do this
print(dict["cities"])
print("currently living in %s"  %dict["cities"][1])

'''
surname is N.P
age is 22
('Saigon', 'San Jose', 'Los Angeles')
currently living in San Jose
'''
