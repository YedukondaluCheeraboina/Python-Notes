#Prtogram for Obtaining List of +Ve values from given List of elements
#ContinueStmtEx5.py
lst=[10,-23,20,-45,67,-11,78,-90,-89,29]
print("List of +Ve Values")
for val in lst:
    if(val<=0):
        continue
    print("\t{}".format(val))
#-------------------------------------------------
