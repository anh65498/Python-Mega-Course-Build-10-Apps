#it's bad to load all the modules and library when run Python so only import them only when needed
#module is library written by Python that when in our program that we need some functions (that we don't use often), then "import" the module that has it
import os
path = "/Users/anhpham/Documents/Udemy/Python with 23 apps/Lessons"                 #terminal $pwd
#to concatanate a lot of text files in a directory into a single files

#to generate a list of file paths in the current directory
print(os.listdir(path))

'''
['.DS_Store', '10_exceptions_handling.py', '11_function.py', '12_conditionals.py', '13
_for_loops.py', '14_while_loops.py', '15_file_handling', '16_modules_library_package.p
y', '17_modules, libraries', '1_variables, data type, functions.py', '2_numbers and ma
th.py', '3_strings.py', '4_string_and_index.py', '5_string_exercise.py', '6_list.py',
'7_list_exercise.py', '8_tuples.py', '9_dictionary.py', 'delete.py', 'delete.txt']
'''
#library: is a collection of module. Sometimes the modules are just too big
