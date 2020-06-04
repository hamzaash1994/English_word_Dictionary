import json
from difflib import get_close_matches 
#load json file
data = json.load(open("english_words_dic\data.json"))
# create a function
def translate(w):
    w = w.lower()
    # create conditionals 
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y for yes and N for no  " % get_close_matches("w", data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "the word don't exist"
        else: 
            return "we did not understand your entry"
    else:
        return "the word doesn't exist. pls double check it."

#Ask the user for an input
word = input("enter word: ")
output = translate(word)
# create conditionals for a clean output 
if type(output) == list:
    for item in output:
        print(item)
else:
    print(item)

