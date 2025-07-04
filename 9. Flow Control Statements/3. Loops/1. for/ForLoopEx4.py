#program for  demonstrating for loop
#ForLoopEx4.py
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("List of  Numbers within:{}".format(n))
    for i in range(1,n+1):
        print("\t{}".format(i))
print("------------------------------------------")
print("List of Even Numbers within:{}".format(n))
for i in range(2,n+1,2):
    print("\t{}".format(i))
print("------------------------------------------")
print("List of Odd Numbers within:{}".format(n))
for i in range(1,n+1,2):
    print("\t{}".format(i))
print("------------------------------------------")


