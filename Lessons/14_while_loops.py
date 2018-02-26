user_password = "Hello world!"
input_password = input("What's your password? ")

while (input_password != user_password):
    print ("Password incorrect")
    input_password = input("Re-enter your password: ")



'''
NameError: name 'dfagtbg' is not defined

Fix: python3 instead of python 2 because input only works in python3. use raw_input for python2

'''
