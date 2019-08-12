import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def definition(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),cutoff=0.75))>0 :
        ans=input( "did you mean {} . type 'Y' if you mean it or type 'N' for no : ".format(get_close_matches(w,data.keys(),cutoff=0.75)[0].upper()))
        if ans.lower()=='y':
            return definition(get_close_matches(w,data.keys(),cutoff=0.75)[0])
        else:
            return "The word doesn't exist"
    else:
        return "The word doesn't exist . Please verify it"


word = input("Enter the word: ")

print(definition(word))
