#Program for Reading Number of Values dynamically from KBD and display
#ReadValuesEx1.py
n=int(input("Enter How Many Values u have:"))
if(n<=0):
    print("\t{} is invalid Input".format(n))
else:
    lst=[] #empty list-for adding values
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("Content of List")
        print(lst)
