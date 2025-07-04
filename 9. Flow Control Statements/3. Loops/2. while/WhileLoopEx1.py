#program for generating 1 to N where N is +Ve
#WhileLoopEx1.py
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Numbers within:{}".format(n))
    print("-" * 50)
    i=1  # Initlization Part
    while(i<=n):  # Test Cond
        print("\t{}".format(i))
        i+=1 # OR i=i+1  ---Updation Part
    else:
        print("-"*50)
    print("Program execution Completed")