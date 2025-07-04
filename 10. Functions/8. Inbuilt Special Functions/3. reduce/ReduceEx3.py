#Program for Accepting List of Values and Find Max and Min
#ReduceEx3.py
import functools
print("Enter List of Numerical separated by space:")
vals=[float(val) for val in input().split() ]
print("Given Values")
print(vals) # 10 2 13 45 6 16 17 23
maxv=functools.reduce(lambda k,v: k if k>v else v, vals )
minv=functools.reduce(lambda k,v: k if k<v else v, vals )
print("Max Value=",maxv)
print("Min Value=",minv)


