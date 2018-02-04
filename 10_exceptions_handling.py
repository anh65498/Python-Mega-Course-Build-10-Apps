#Goal: learn to debug
#2 types of errors in Python: Syntax Errors and Exceptions

def divide(a,b):
    try:
        return a /b;                    #execute these command unless exception occur
    except ZeroDivisionError:
        return ("You are dividing by zero")

print(divide(1,0))
print("After catching exception, the program proceeds")
