#icici.py<---File Name and acts as Module Name
bname="ICICI"
addr="Ampt-HYD" # bname and addr are called Global Var
def simpleint(): # Function Def
    p=float(input("Enter Principle Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter rate of Interest:"))
    #cal si
    si=(p*t*r)/100
    totamt=p+si
    print("-"*50)
    print("\tPrinciple Amount:{}".format(p))
    print("\tTime:{}".format(t))
    print("\tRate of Interest:{}".format(r))
    print("\tSimple interest:{}".format(si))
    print("\tTotal Amount:{}".format(totamt))
    print("-" * 50)

