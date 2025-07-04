#program for accepting Three Numerical values and Find Bigest
#SimpleIfStmtEx2.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
if(a>=b) and (a>c):
    print("Max({},{},{})={}".format(a,b,c,a))
if(b>a) and (b>=c):
    print("Max({},{},{})={}".format(a, b, c, b))
if(c>=a) and (c>b):
    print("Max({},{},{})={}".format(a,b,c,c))
if(a==b) and (b==c) and (c==a):
    print("All Values are equal")





