#program for deciding whether the given number is prime or not
#BreakStmtEx6.py
n=int(input("Enter a Number :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    res="PRIME" if res else "NOT PRIME"
    print("{} is {}".format(n,res))
