#program for Finding Frequency of Every Letter of Given word
#NumberOccurencesEx1.py
word=input("Enter a Word:")
if(len(word)==0):
    print("\tGiven word is Empty-u must enter a word:")
else:
    print("Given Word:",word) # word =MISSISSIPPI
    d={} # empty dict for storing Letter and its Frequency
    for ch in word:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]=d[ch]+1 # d[ch]=d.get(ch)+1

    else:
        for k,v in d.items():
            print("\t{}--->{}".format(k,v))



