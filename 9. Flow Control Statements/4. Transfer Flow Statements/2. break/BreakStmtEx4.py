#Program for Demonstrating the need of break statement.
#BreakStmtEx4.py
s="MISSISSIPPI"
print("-------------------------------------")
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-------------------------------------")
#-------------------------------------------------
#Today My Req : To display 'MISS'
print("-------------------------------------")
print("By using while Loop")
i=0
ctr=0
while(i<len(s)): # s="MISSISSIPPI"
    if(s[i]=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print("{}".format(s[i]),end="")
    i=i+1
