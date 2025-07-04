#program for generating  N  to 1 where N is +Ve
#WhileLoopEx2.py
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("*" * 50)
    print("Numbers from {} to {}".format(n,1))
    print("*" * 50)
    i=n # Initlization part
    while(i>=1):
        print("\t{}".format(i))
        i-=1 # OR i=i-1
    else:
        print("*"*50)

