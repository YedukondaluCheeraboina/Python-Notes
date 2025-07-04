#Program for accepting a word / value and decide whether It is Palindrome or Not
#By using anonymousFunction
#AnonymousFunEx2.py
palindrome=lambda val: "Palindrome" if val==val[::-1] else "Not Palindrome"
#Main Program
value=input("Enter Any Value:")
res=palindrome(value) # Anonymous function call
print("{} is {}".format(value,res))