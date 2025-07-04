#Program for accepting Line of Text and Display Its words
#WordsFromLine.py
line=input("Enter Line of Text:")
print("Given Line=",line)
words=line.split()
for word in words:
    print("\t{}".format(word))
