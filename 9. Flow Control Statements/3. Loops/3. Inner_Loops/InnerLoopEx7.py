#Program for Listing the Prime Values within the range
#InnerLoopEx7.py
ranval=int(input("Enter the Range Value in which u want primes:")) # 10
if(ranval<=1):
    print("\t{} is Invalid ".format(ranval))
else:
    print("-"*40)
    print("List of Primes within:{}".format(ranval))
    print("-" * 40)
    for num in range(2,ranval+1): # Supply the Value--outer
        res=True
        for i in range(2,num): # inner loop
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t{}".format(num))
    print("-" * 40)


