#Program for accepting Two Numerical vals and find big among them and check for equality
#By using anonymousFunction
#AnonymousFunEx3.py
bigv=lambda k,v:k if k>v else v if v>k else "Both Values are equal"

#main Program
a=float(input("Enter First Value:"))
b=float(input("Enter First Value:"))
bv=bigv(a,b)
print("Max({},{})={}".format(a,b,bv))
