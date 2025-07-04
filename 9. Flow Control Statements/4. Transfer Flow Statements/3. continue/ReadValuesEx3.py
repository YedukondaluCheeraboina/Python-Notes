#Program for Reading Number of Values dynamically from KBD and display
#ReadValuesEx3.py
print("Enter Number of Values (Press @ to stop):")
lst=list() # empty list
while(True):
    value=input()
    if(value!="@"):
        lst.append(float(value))
    else:
        break

print("List of Values")
print(lst)


