#Program for Cal simple Interest and total amount to Pay
#ArithmeticOperatorsEx2.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#Cal si and totamt to pay
si=(p*t*r)/100
totamt=p+si
print("-"*50)
print("\tResults of Simple Interest")
print("-"*50)
print("\tPrinciple Amount:{}".format(p))
print("\tTime:{}".format(t))
print("\tRate of Interest:{}".format(r))
print("\tSimple Interest:{}".format(si))
print("\tTotal Amount to Pay:{}".format(totamt))
print("-"*50)