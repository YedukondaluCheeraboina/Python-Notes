#Program for Demonstrating the need of break statement.
#BreakStmtEx2.py
s="PYTHON"
print("-------------------------------------")
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-------------------------------------")
#---------------------------------------------------
#Today my req to display: PYTH without using Indexing and Slicing
i=0
while(i<len(s)): # s=PYTHON
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i=i+1
else:
    print("I am from else part of while loop")
print()
print("Program execution completed")

