#Program for Finding sum of First N Natural Numbers.
#ForLoopEx6.py
n=int(input("Enter How Natural Nums Sum U want to Find:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Natural Numbers within:{}".format(n))
    p=0 # Additive Identity--Keeps Track of repeated sum
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p+i
    else:
        print("-"*50)
        print("sum={}".format(p))
        print("-" * 50)