#program for accepting a word and decide whether It is Vowel OR Not
#BreakStmtEx8.py
word=input("Enter a Word:") # s="WHY"
res="NOT VOWEL"
for ch in word:
    if(ch.lower() in ["a","e","i","o","u"]):
        res="VOWEL"
        break
print("{} is {} word".format(word,res))

