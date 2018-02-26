#python can handle both binary file (dhl file) and text file

input_file_name = "input_file.txt"
file = open(input_file_name, 'r');
print ("Type of file", type(file));     #('Type of file', <type 'file'>)

#content of the file, all saves in a string
content = file.read();
print("Content of %s"   %input_file_name)
print(content)


#Save lines in a list instead of string
list_of_line = file.readline()
print("Content of %s"   %input_file_name)
print(list_of_line)
print("can't print because the pointer is at the end of the file after the previous read")
print("to fix that, use file.seek()")

file.seek(0)
list_of_line = file.readlines()
print("Content of %s"   %input_file_name)
print(list_of_line)

'''
['            GORGEOUS\n', 'You should take it as a compliment\n', 'Tha
t I got drunk and made fun of the way you talk\n', 'You should think ab
out the consequence\n', 'Of your magnetic field being a little too stro
ng\n', '\n', 'Whisky on ice, Sunset and Vine\n', "You've ruined my life
, by not being mine\n"]
'''

#remove \n from all the string in list_of_lines
new_list = [i.rstrip("\n") for i in list_of_line]
print (new_list)
'''
['            GORGEOUS', 'You should take it as
a compliment', 'That I got drunk and made fun of
 the way you talk', 'You should think about the
consequence', 'Of your magnetic field being a li
ttle too strong', '', 'Whisky on ice, Sunset and
 Vine', "You've ruined my life, by not being min
e"'''

#if you don't close the file, any changes made to the file will not be saved
file.close()
