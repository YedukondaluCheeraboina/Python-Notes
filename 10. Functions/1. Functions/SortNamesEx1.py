#Program for accepting List of Names and sort then Both Ascending and Decending Order
#SortNamesEx1.py
def readnames():
    non=int(input("Enter How Many Names u want to sort:"))
    if(non<=0):
        return list()
    else:
        nameslist=list()
        for i in range(1,non+1):
            name=input("Enter {} Name:".format(i))
            nameslist.append(name)
        return nameslist
def dispnames(nameslist,order):
    print("-----------------------------")
    print(order)
    print("-----------------------------")
    for names in nameslist:
        print("\t{}".format(names))
    print("-----------------------------")

def sortnames(nameslist):
    if(len(nameslist)==0):
        print("List is empty--can't Sort")
    else:
        dispnames(nameslist,"Original Names") # Function call
        nameslist.sort() # Ascending order
        dispnames(nameslist,"Names in Asceding order")
        nameslist.sort(reverse=True)  # Decending  order
        dispnames(nameslist, "Names in Decending Order")

#main Program
names=readnames() # Function call
sortnames(names) # Function call
