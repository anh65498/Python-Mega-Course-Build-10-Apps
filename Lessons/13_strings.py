age = input("Enter your age: ");
new_age = float(age) + 50;
print (new_age);

greeting = "Hi there Peter!"
print ("replacing 'e' in %s with 'i'"  %(greeting))
greeting = greeting.replace("e", "i");
print(greeting);
#print dir(greeting);       #can't do this


input("Press Enter to continue");
greeting2 = "Hi there Peter!"
greeting2 = greeting2.replace("e", "a", 2);
print ("replacing 2 'e' in %s with 'a'"  %(greeting2))
print (greeting2);



''' dir(object)  returns a list of attribute of that object. Example:
greeting = "Hi there"
>>> dir(greeting)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc_
_', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '
__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '_
_iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '
__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__
', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize
', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'fin
d', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'i
sdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'p
artition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title
', 'translate', 'upper', 'zfill']

>>> help("".upper)
upper(...) method of builtins.str instance
    S.upper() -> str

    Return a copy of S converted to uppercase.
>>> help("".replace)
replace(...) method of builtins.str instance
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
'''
