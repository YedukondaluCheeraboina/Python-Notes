#program for generating all even numbers within in N
#WhileLoopEx5.py
n=int(input("Enter How Many Even Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Even Numbers within :{}".format(n))
    print("-" * 50)
    i=2
    while(i<=n):
        print("\t{}".format(i))
        i+=2#OR i=i+2
    else:
        print("-" * 50)

