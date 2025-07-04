#program for Demonstrating the Need of Continue Statement
#ContinueStmtEx2.py
s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of for loop")
#------------------------------------------
#Today: My Req: PYHON
i=0
while(i<len(s)): # s="PYTHON"
    if(s[i]=="T"):
        i=i+1
        continue
        #i=i+1--Can't execute
    print(s[i],end="")
    i=i+1
else:
    print()
    print("I am from else part of for loop")
#------------------------------------------