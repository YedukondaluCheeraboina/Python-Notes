#Program for Swapping of any Two Integer Values--Logic-2
#AssignmentOp3.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
print("-"*50)
#Swapping Logic
a=a+b
b=a-b
a=a-b
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("-"*50)
