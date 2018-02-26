'''
Purpose: Build a program which you can give an English word and the program will return the definition of that word in English

Receive: input (English word) from user via command line interface
Return: definition

Features:
    + if a word has 2 meanings, return both
    + if user mistype input, suggest the closest word and ask for confirmation
    + if the word doesn't exist, alert

Future features:
    + web application instead of command line application

Mechanism: search words and extract its definition(s) from data.json. Data.js is a data set of words and definition. it is heavy 5 megabytes so Atom will "freeze" for 1 minutes
'''

#What? Load data.json into a python dictionary (because of similar structure)
#How? Use JSON standard library
import json
data = json.load(open("data.json"))          #since load(fp) where fp is a file-like object, use "open()" to create it

#function that get an input as key and return the value for that key
def get_definition(key):
    return data[key]
