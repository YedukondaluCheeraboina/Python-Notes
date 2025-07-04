#Demonstrating ATM Amount Dispatching the Notes
#ArithmeticOperatorsEx.py
wamt=int(input("Enter How Much Amount u want to Withdraw:"))
#-----------------------
rs500=wamt//500
wamt=wamt%500
#-----------------------
rs200=wamt//200
wamt=wamt%200
#-----------------------
rs100=wamt//100
wamt=wamt%100
print("-"*50)
print("Dispencing Cash deatils")
print("\tNumber of 500:{}".format(rs500))
print("\tNumber of 200:{}".format(rs200))
print("\tNumber of 100:{}".format(rs100))
print("-"*50)