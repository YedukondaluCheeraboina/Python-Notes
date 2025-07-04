#AnonymousFunEx1.py
def sumop(a, b): # By using Normal Function
    return a + b

addop = lambda a,b:a+b   # Anonymous Function

# Main Program
print("Type of sumop=",type(sumop)) # <class, function>
res = sumop(10, 20)
print("sum=", res)
print("---------------------------------------")
print("Type of addop=",type(addop))# <class, function>
res1=addop(100,200)
print("Sum by using anonymous fun=",res1)
