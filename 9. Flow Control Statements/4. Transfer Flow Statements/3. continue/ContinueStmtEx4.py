#program for Demonstrating the Need of Continue Statement
#ContinueStmtEx4.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
#------------------------------------------
#Today: My Req: PYHN
for ch in s:
    if(ch in ["T","O"] ):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")