#program for accepting Two Numerical values and Find Bigest
#SimpleIfStmtEx1.py
a=float(input("Enter Value of a:")) #a=10
b=float(input("Enter Value of b:"))# b=20
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
    print("Big({},{})={}".format(a, b, b))
if(a==b):
    print("Both Values are equal")
print("Program Execution Completed")