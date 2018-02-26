#create a new file call example2.txt if it is not already created
#"w" mode will wiped out all of the content of example2.txt
in_file = open("example2.txt", "w")

#add these lines to "example2.txt". Feel free to change them and see the difference
in_file.write("\t\tWithout a Trace - Kill The Noise\n")
in_file.write("As a child I ran from home\n")
in_file.write("Eyes are tired, my soul is bored\n")

#add a list of strings to example2.txt
list = ["Da da la da day and night", "Say the words and you'll be fine",
        "I fell for you, what have I become", "I can't imagine, the truth\n"]
for item in list:
    in_file.write(item+"\n");
#note "+ '\n'" instead of adding \n at the end of each line


#close the file to save changes to "example2"
in_file.close()

#append to the end of file
file = in_file.open("example2.txt","a")
file.write("Let me fall, all the way\n")
file.write("Without a trace, without a trace")

'''
"r"     open a file for reading only. The file pointer is placed at the beginning of the file. Default mode
"r+"    open a file for both reading and writing. The file pointer is placed at the beginning of the in_file
"w"     open a file for writing only. Overwrite the file if it already exists. If the file does not exist, create a file for writing
"w+"    open a file for both writing and reading. Overwrite the file if it already exists. If the file does not exist, create a file for writing
"a"     open a file for appending. The file pointer is at the end of the file if the file exists.
"a+"    open a file for both reading and appending. The file pointer is at the end of the file if the file exists.
'''
