#Define the Function for addition of Two Numbers
#INPUT-------------->Taking from Function Call
#PROCESS------------>Process Done in Function Body
#OUTPUT------------->Displayed in Function Body
#ApproachEx3.py
def sumop(a,b):
    c=a+b
    print("Sum({},{})={}".format(a,b,c))

#Main Program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
sumop(a,b) # Function Call