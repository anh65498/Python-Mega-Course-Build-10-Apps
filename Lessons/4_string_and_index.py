string = "Hey there!"
#every item in your string has an index

#accessing an element(letter, space, number) in list
print (string[0])                    #H

#return the type of an object
print (type(string[4]));             #<class 'str'>

#accessing an element from last element
print (string[-1])                  #last element of index
print (string[-2])                  #second last element

#print all elements in string last to first
print (len(string));
# for (int i = -1; i <= * -1)

#create a substring
hey = string[0:3]
print (hey)     #hey

#create a substring from starting -> end
there = string[4:]
print (there)      #there!

#create a substring
re = string[-3:-1]      #because upperbound is exclusive
print(re)               #re
