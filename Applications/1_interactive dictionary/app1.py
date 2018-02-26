#What? Load data.json into a python dictionary (because of similar structure)
#How? Use JSON standard library
#Learn? SequenceMatcher module, a module to find
import json
from difflib import SequenceMatcher        #module to compare text, need for sequencematcher
dictionary = json.load(open("data.json", "r"))          #since load(fp) where fp is a file-like object, use "open()" to create it

#receive: word(string) to look up
#return: definition of that word
def get_definition(word):
    if word.lower() in dictionary:
        return dictionary[word]
    else:
        return "The word doesn't exist. Please double check it."

#get word to look up from user
word = input("Enter word you want to look up: ")

#display definition to command line
print(get_definition(word))
