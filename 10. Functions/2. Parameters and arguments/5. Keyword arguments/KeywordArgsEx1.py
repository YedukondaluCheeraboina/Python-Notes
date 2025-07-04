#program for Demonstrating Key words args
#KeywordArgsEx1.py
def dispvals(a,b,c,d):
	print('\t{}\t{}\t{}\t{}'.format(a,b,c,d))

#Main Program
print('='*50)
print("\tA\tB\tC\tD")
print('='*50)
dispvals(10,20,30,40) # Function call with pos Args
dispvals(10,20,d=40,c=30)# Function call with pos Args with Keyword args
dispvals(c=30,d=40,b=20,a=10)# Function call with Keyword args
#dispvals(b=20,d=40,c=30,10)---SyntaxError: positional argument follows keyword argument
dispvals(b=20,d=40,c=30,a=10)# Function call with Keyword args
print('='*50)