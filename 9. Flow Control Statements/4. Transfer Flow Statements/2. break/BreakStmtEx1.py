#Program for Demonstrating the need of break statement.
#BreakStmtEx1.py
s="PYTHON"
print("-------------------------------------")
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("-------------------------------------")
#---------------------------------------------------
#Today my req to display: PYTH without using Indexing and Slicing
for ch in s: # s=PYTHON
    if(ch=="O"):
        break
    print(ch,end="")
else:
    print("I am from else part of for loop")
print()
print("Program execution completed")

