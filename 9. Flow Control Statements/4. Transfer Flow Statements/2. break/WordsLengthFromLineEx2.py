#Program for accepting Line of Text and Display Its words
#and find length of each word
#WordsLengthFromLineEx1.py
line=input("Enter a Line of Text:")
words=line.split()
d={} # empty dict--for placing word and its length
for word in words:
    d[word]=len(word)
else:
    print("-"*50)
    print("\tWord\t\tLenght")
    print("-" * 50)
    for W,L in d.items():
        print("\t{}\t\t{}".format(W,L))
    else:
        print("-" * 50)