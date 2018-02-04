#string can only contains substring
#list can contain many data types : letter, number, string, object,

class Animal:
        def __init__(self): pass;


cat = Animal();

list = ["Hi", 2134, "m", cat, -434.23]

#accessing an element in the list
print(list[1]);                   #2134

#determine the type of the last element in the list
print (type(list[-1]));         #<class 'float'>

#create a sub-list from a list
sublist = list[2:4]
print(sublist);                 #['m', <__main__.Animal object at 0x1022832e8>]
print(type(sublist))            #<class 'list'>

#copy list
copy = list;
for i in range (0,len(list)):
    print(copy[i])
#remove an element from the list
#print ()


#more commands
# A = [x for x in range(1, 5)]
# S = [6, 7, 8]
# B = [x for x in S]
'''
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__
dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '
__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '_
_init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '
__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed
__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '_
_subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', '
insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(list.append)
Help on method_descriptor:

append(...)
    L.append(object) -> None -- append object to end
(END)
'''
