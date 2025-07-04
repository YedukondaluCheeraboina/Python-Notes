#program for Demonstrating the Need of Continue Statement
#ContinueStmtEx3.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
#------------------------------------------
#Today: My Req: PYHN
for ch in s:
    if(ch=="T") or (ch=="O"):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")