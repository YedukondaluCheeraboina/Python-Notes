#program for generating  N  to 1 where N is +Ve
#WhileLoopEx3.py
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("*" * 50)
    print("Numbers from {} to {}".format(n,1))
    print("*" * 50)
    while(n>=1):
        print("\t{}".format(n))
        n-=1 # OR n=n-1
    else:
        print("*"*50)

