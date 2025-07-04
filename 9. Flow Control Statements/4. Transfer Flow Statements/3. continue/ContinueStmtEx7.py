#Program for accepting a Line / word and obtains only Vowels
#ContinueStmtEx7.py
word=input("Enter a word:") # word="PYTHON"
for ch in word:
    if ch.lower() not in ['a','e','i','o','u']:
        continue
    print("{}".format(ch),end="")


