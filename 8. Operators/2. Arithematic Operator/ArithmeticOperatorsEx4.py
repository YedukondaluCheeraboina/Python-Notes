#Program for Cal Square of a Given Number
# without using Pre-Defined Function sqrt() of math module
#ArithmeticOperatorsEx4.py
import math
n=float(input("Enter a Number for Cal Square root:"))
res=n**0.5  # OR   res=n**(1/2)
print("Sqrt({})={}".format(n,res))
print("--------------------OR-----------------------")
print("Sqrt({})={}".format(n,round(res,2)))
