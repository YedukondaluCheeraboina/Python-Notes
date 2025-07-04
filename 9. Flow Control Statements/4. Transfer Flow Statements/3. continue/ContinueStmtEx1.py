#program for Demonstrating the Need of Continue Statement
#ContinueStmtEx1.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
#------------------------------------------
#Today: My Req: PYHON
for ch in s: # s="PYTHON"
    if(ch=="T"):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")
#------------------------------------------