#DictCompEx2.py
line=input("Enter a line of Text:")
words=line.split()
dobj={ word:len(word)    for word in words}
for word,wlength in dobj.items():
	print("\t{}--->{}".format(word,wlength))