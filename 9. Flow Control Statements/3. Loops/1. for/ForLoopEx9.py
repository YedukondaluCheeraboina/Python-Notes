#Program for Finding Fcatorial of a Number
#N!= 1 x 2 x 3 x......N
#OR   N x N-1 x N-2........0!
# 0!= 1
#ForLoopEx8.py
n=int(input("Enter a Number for Finding Factorial:"))
if(n<0):
    print("\t{} is -VE Value--can't cal Factrial".format(n))
else:
    fact=1
    for i in range(1,n+1):
        fact*=i # OR fact=fact*i
    else:
        print("factroail({})={}".format(n,fact))



