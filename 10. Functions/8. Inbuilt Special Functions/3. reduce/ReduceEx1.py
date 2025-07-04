#Program for Accepting List of Values and Find Their sum by using reduce()
#ReduceEx1.py
import functools
def sumop(k,v):
    return(k+v)

#main program
print("Enter List of Numerical separated by space:")
vals=[float(val) for val in input().split() ]
print("Given Values")
print(vals)
res=functools.reduce(sumop,vals)
print("sum=",res)

