#Program for Converting word or line of text into lower case
#Without using pre-defined Function
#ConvertIntoLower.py
line=input("Enter Line of Text:") # PYtHoN
print("Given Line={}".format(line))
lc=""
for ch in line:
    if ord(ch) in range(65,91):
        lc=lc+chr(ord(ch)+32)
    else:
        lc=lc+ch
else:
    print("Lower Case=",lc)


