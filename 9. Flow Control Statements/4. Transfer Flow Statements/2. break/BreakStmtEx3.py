#Program for Demonstrating the need of break statement.
#BreakStmtEx3.py
s="MISSISSIPPI"
print("-------------------------------------")
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("-------------------------------------")
#-------------------------------------------------
#Today My Req : To display 'MISS'
print("-------------------------------------")
print("By using for Loop")
ctr=0
for ch in s: # s="MISSISSIPPI"
    if(ch=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print("{}".format(ch),end="")
