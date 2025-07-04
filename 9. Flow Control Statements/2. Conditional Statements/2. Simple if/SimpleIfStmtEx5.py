#Program for Calculating Simple Interest
# provided all values (p,t,r) values are +Ve
#otherwise Corresponding Error Messages
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
if(p>0) and (t>0) and (r>0):
    si=(p*t*r)/100
    totamt=p+si
    print("-"*50)
    print("\tPrinciple Amount:{}".format(p))
    print("\tTime:{}".format(t))
    print("\tRate of Interest:{}".format(r))
    print("\tSimple interest:{}".format(si))
    print("\tTotal Amount to Pay:{}".format(totamt))
    print("-" * 50)
if(p<=0):
    print("\tprinciple Amount :{} is Invalid".format(p))
if(t<=0):
    print("\tTime :{} is Invalid".format(t))
if(r<=0):
    print("\tRate of Interest :{} is Invalid".format(r))

