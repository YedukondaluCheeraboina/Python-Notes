#program for Generating 1 to N mul Tables
#InnerLoopEx5.py
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    for num in range(1,n+1): # outer loop--Supply the Number
        print("-" * 50)
        print("Mul Table for:{}".format(num))
        print("-" * 50)
        for i in range(1,11): # inner loop--Display Mul Table
            print("\t{} x {} = {}".format(num,i,num*i))
        else:
            print("-"*50)

