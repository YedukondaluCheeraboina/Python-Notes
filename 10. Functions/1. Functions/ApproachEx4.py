#Define the Function for addition of Two Numbers
#INPUT-------------->Taking Input in Function Body
#PROCESS------------>Process Done in Function Body
#OUTPUT------------->Giving to Fucntion Call
#ApproachEx4.py
def sumop():
    # Taking Input
    k = float(input("Enter First Value:"))
    v = float(input("Enter Second Value:"))
    # Process
    r = k + v
    #give the result back to Function call
    return k,v,r
    # return stmt can return either one val or more than one value
#Main Program
a,b,c=sumop() # Function Call with multi Line assignment
print("Sum({},{})={}".format(a,b,c))
print("----------OR--------------")
res=sumop() # function call with single line assignment
#Here res is an object of type <class,tuple>
print("Sum({},{})={}".format(res[0],res[1],res[2]))
print("------------OR-------------")
print("Sum({},{})={}".format(res[-3],res[-2],res[-1]))