import json
from difflib import get_close_matches

# load json data
data = json.load(open("resources/data.json"))

def translate(w):
    w = w.lower()
    matches = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(matches) > 0:
        choice = input("are you looking for the word %s ? Enter Y if yes, or N if no: " % matches[0])
        if choice == 'Y' or choice == 'y':
            return data[matches[0]]
        elif choice == "N" or choice == 'n':
            return "The word doesn't exist!"
        else:
            return "We didn't understand the word you entered!!!"
    else:
        return "The word doesn't exist!"

# global variable
word = input("Enter the word: ")

match_words = translate(word)

if type(match_words) is list:
    for item in match_words:
        print(item)
else:
    print(match_words)