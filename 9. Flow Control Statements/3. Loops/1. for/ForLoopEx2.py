#program for Demonstarting for Loop
#ForLoopEx2.py
s="PYTHON"
print("----------------------------------")
print("By using for loop--Logic-1--Forward Direction")
for ch in s: # s=PYTHON
    print("\t{}".format(ch))
print("----------------------------------")
print("By using for loop--Logic-2--Forward Direction with +ve Index")
for i in range(len(s)):
    print("\t{}".format(s[i]))
print("----------------------------------")
print("By using for loop--Logic-3--Forward Direction with -ve Index")
for i in range(-len(s),0):
    print("\t{}".format(s[i]))
print("----------------------------------")
print("By using for loop--Logic-4--Backward Direction")
for ch in s[::-1]: # s=PYTHON
    print("\t{}".format(ch))
print("----------------------------------")
print("By using for loop--Logic-5--Backward Direction with +ve Index ")
for i in range(len(s)-1,-1,-1):
    print("\t{}".format(s[i]))
print("----------------------------------")
print("By using for loop--Logic-6--Backward Direction with -ve Index ")
for i in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[i]))
print("----------------------------------")