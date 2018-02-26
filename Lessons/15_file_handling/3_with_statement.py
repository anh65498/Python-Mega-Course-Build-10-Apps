#with let you write cleaner code when handling false
#is used to wrap the execution of a block with methods defined by a context manager

input_file_name = "example3.txt"
#doesn't have to close the file at the end
with open(input_file_name, "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\t\tI can't escape\n")
    file.write("Why am i feeling so cold?\nLost myself for the night\nI can feel in my bones\n")
    print(content)
