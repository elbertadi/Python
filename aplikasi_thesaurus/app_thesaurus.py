import json
from difflib import get_close_matches

data = json.load(open("aplikasi_thesaurus/data.json"))

def arti(word):
    u = word.lower()
    if u in data:
        return data[u]
    elif len(get_close_matches(u, data.keys())) > 0:
        print ("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(u, data.keys())[0])
        hasil = input("")
        if (hasil == "Y"):
            y = get_close_matches(u, data.keys())[0]
            return data[y]
        elif (hasil == "N"):
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = (arti(word))

if(type(output) == list):
    for item in output:
        print(item)
else:
    print(output)