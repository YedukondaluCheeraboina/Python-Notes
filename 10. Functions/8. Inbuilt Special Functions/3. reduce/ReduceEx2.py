#Program for Accepting List of Values and Find Their sum by using reduce()
#ReduceEx2.py
import functools
print("Enter List of Numerical separated by space:")
vals=[float(val) for val in input().split() ]
print("Given Values")
print(vals)
res=functools.reduce(lambda k,v:k+v,vals)
print("sum=",res)

