#program for Obtaining List of Unique Values from given List of Values
#by using set()
#UniueValuesEx1.py
print("Enter Number of Values (Press @ to stop):")
lst=list() # empty list
while(True):
    value=input()
    if(value!="@"):
        lst.append(float(value))
    else:
        break
print("---------------------------")
print("List of Values")
print(lst)
#lst=[10.0, 20.0, 10.0, 20.0, 30.0, 40.0, 10.0, 20.0, 30.0, 50.0, 60.0]
print("---------------------------")
ulist=list() # for placing Unique Values
for val in lst:
    if val not in ulist:
        ulist.append(val)
else:
    print("List of Unique Values")
    print(ulist)


