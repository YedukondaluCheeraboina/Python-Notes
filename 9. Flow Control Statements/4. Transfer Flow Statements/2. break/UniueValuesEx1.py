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
print("---------------------------")
s=set(lst) # Convert List of Values into set type.
print("Unique Values")
print(s)

