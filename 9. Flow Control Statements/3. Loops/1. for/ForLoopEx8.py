#Program for Finding Product of First N Natural Numbers.
#ForLoopEx8.py
n=int(input("Enter How Natural Nums Product U want to Find:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Natural Numbers within:{}".format(n))
    p=1 # Multiplicative Identity--Keeps Track of repeated Product
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p*i
    else:
        print("-"*50)
        print("Product={}".format(p))
        print("-" * 50)