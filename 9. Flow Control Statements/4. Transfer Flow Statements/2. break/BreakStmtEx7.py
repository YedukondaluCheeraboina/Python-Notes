#program for deciding whether the given number is prime or not
#BreakStmtEx7.py
n=int(input("Enter a Number :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res=True
    i=2
    while(i<n):
        if(n%i==0):
            res=False
            break
        i=i+1
    res="PRIME" if res else "NOT PRIME"
    print("{} is {}".format(n,res))
