#program for Demonstarting for Loop
#ForLoopEx1.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
print("----------------------------------")
print("By using for loop")
for ch in s: # s=PYTHON
    print("\t{}".format(ch))
else:
    print("----------------------------------")