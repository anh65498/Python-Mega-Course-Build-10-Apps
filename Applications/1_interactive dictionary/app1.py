#What? Load data.json into a python dictionary (because of similar structure)
#How? Use JSON standard library
#Learn? SequenceMatcher module, a module to find
import json
from difflib import SequenceMatcher        #module to compare text and find close matches
from difflib import get_close_matches
dictionary = json.load(open("data.json", "r"))          #since load(fp) where fp is a file-like object, use "open()" to create it

#receive: word(string) to look up
#return: definition of that word
def get_definition(word):
    if word.lower() in dictionary:
        return dictionary[word]
    elif len(get_close_matches(word,dictionary.keys())) > 0:
        suggestion = get_close_matches(word, dictionary.keys())[0]
        decision = input("Can't find %s. Did you mean %s. Y/N? " %(word, suggestion))
        #dictionary.keys( ) returns a list of all keys in dictionary
        if decision.lower() == "y" or decision.lower() == "yes":        #decision.lower() == "y" or "yes" does not work :( s
            return dictionary[suggestion]
        elif decision.lower() == "n" or decision.lower() == "no":
            return("The word doesn't exist. Please double check it.")
        else:
            return "I do not understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


def main():
    #get a word to look up from user
    word = input("Enter word you want to look up: ")

    #get definition from get_definition()
    definition = get_definition(word)

    #display definition to screen
    if (type(definition)) == list:          #print list of definition
        for i in definition:
            print("-", i)
    else:                                   #print errors
        print(definition)

    return input("Do you want to look up another word? Y/N? ")

redo = "yes"
while (redo.lower() == "yes" or redo.lower() == "y"):
    redo = main()


#print(SequenceMatcher(None, "rain", "rainn").ratio( ))
##ratio returns the similarity between the two strings  (0 -> 1)
##SequenceMatcher's first argument is None or a function to ignore line breaks/whitespaces/markups ... between the two strings.
##In our case, we don't have those "junk" data in our two strings,  so don't need a function. Hence, "None"

#get_close_matches returns a returns a dict_key objects, but behaves like a list, of words similar to first argument from second arg
#cuttoff is similarity's ratio
