#Program for accepting Line of Text and Display Its words
#and find length of each word
#WordsLengthFromLineEx1.py
line=input("Enter a Line of Text:")
words=line.split()
for word in words:
    print("\t{}--->{}".format(word,len(word)))