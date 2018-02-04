#tuples are not mutable. There's no tuple.insert(), tuple.append(), tuple.remove(), tuple.pop() .... method that can change the tuple
#list are used more than tuples. but tuples are used in specific scenarios
#tuple can contain different data types too

#create a tuple
tuple = ("Hello", -3, 4.5);

#accessing the last element of tuple's elements
print(tuple[-1]);

#print all elements in tuple
for i in range(0, len(tuple)):
    print(tuple[i])
