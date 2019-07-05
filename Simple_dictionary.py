import json
from difflib import SequenceMatcher
data = json.load(open("data.json"))
def get_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        for w in data:
            similarity_ratio = SequenceMatcher(None, word , w).ratio()
            if (float(similarity_ratio) > 0.7) :
                print("did you mean %s ? " % w )
                decision = input("type y for yes or n for no or h for home : \t")
                if decision == "y":
                    return data[w]
                elif decision == "h":
                    return "Back to home"
                else:
                    print("checking...")
            else:
                continue
        return "This is Not Even A WOOORD!!!!"

while(1):
    word = str(input("Enter a word:"))
    if word != "q":
        print(get_meaning(word))
        print("type 'q' to exit program")
    else:
        break
