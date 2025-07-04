#Program for accepting List of Numerical vals and find big among them
#By using anonymousFunction
#AnonymousFunEx4.py

findmax=lambda lst:max(lst) # Anonymous function uses pre-defined fucntion

#main Program
print("Enter List of Values separated by comma:")
lst=[float(val) for val in input().split(",")] # list Comprehension
print("Given List of Values")
print(lst)
maxv=findmax(lst)
print("Max value=",maxv)