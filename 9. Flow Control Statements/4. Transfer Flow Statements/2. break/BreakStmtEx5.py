#program for deciding whether the given number is prime or not
#BreakStmtEx5.py
n=int(input("Enter a Number :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("{} is {}".format(n,res))
