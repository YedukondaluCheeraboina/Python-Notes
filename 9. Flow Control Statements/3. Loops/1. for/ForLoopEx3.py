#program for Displaying the Values of List and dict by using for loop
#ForLoopEx3.py
print("---------------------------------------")
lst=[100,"Swathi","Delhi",34.56,"Python"]
for value in lst:
    print("\t{}".format(value))
print("---------------------------------------")
d={10:"mango",20:"Apple",30:"Sberry",40:"Kiwi"}
for x in d:
    print("\t{}--->{}".format(x,d[x]))
print("---------------------------------------")
d={10:"mango",20:"Apple",30:"Sberry",40:"Kiwi"}
for x in d:
    print("\t{}--->{}".format(x,d.get(x)))
print("---------------------------------------")