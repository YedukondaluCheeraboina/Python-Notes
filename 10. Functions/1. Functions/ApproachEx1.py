#Define the Function for addition of Two Numbers
#INPUT-------------->Taking from Function Call
#PROCESS------------>Inside of Function Body
#OUTPUT------------->Giving to Fucntion Call
#ApproachEx1.py
def sumop(a,b):
    c=a+b
    return c

#main Program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=sumop(a,b) # Function Call
print("Sum({},{})={}".format(a,b,c))
print("----------------------------------------")
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
r=sumop(k,v) # Function Call
print("Sum({},{})={}".format(k,v,r))
