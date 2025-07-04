#Program for accepting List of Numerical vals and find big among them
#By using anonymousFunction
#AnonymousFunEx4.py
def kvrmax(lst): # lst[10,12,3,14,24,13]
    maxv=lst[0]
    for val in lst:
        if(val>maxv):
            maxv=val
    return maxv

findmax=lambda lst:kvrmax(lst) # Anonymous function uses Programmer-defined fucntion
checkequality=lambda lst:"All Values are Equal" if (len(set(lst))==1) else findmax(lst)

#main Program
print("Enter List of Values separated by comma:")
lst=[float(val) for val in input().split(",")] # list Comprehension
print("Given List of Values")
print(lst)
maxv=checkequality(lst)
print("Max value=",maxv)