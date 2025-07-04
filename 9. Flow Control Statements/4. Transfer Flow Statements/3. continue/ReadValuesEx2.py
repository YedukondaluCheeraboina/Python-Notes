#Program for Reading Number of Values dynamically from KBD and display
#ReadValuesEx2.py
n=int(input("Enter How Many Names u have:"))
if(n<=0):
    print("\t{} is invalid Input".format(n))
else:
    lst=[] #empty list-for adding values
    for i in range(1,n+1):
        value=input("Enter {} Name:".format(i))
        lst.append(value)
    else:
        print("List of Names")
        print(lst)
