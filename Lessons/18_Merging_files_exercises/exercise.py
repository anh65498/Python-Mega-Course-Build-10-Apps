'''
 Consider using the glob third-party library to generate a list of filenames (file1, file2, file3 in the same folder) to iterate through.

2. Use a "with" statement to create a new text file and then iterate through the file list inside that "with" statement and open and read existing file contents in each iteration and write them to new text file.
'''

#generate a list of filenames
import glob         #finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
import datetime

#create an list of files' names
filenames_list =glob.glob("*.txt")

with open(datetime.datetime.now().strftime("%m %d %Y %I-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames_list:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
