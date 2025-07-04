#Program for Demonstrating the need of Variable Length Arguments
#This Program will not execute as It is bcoz PVM Remebers Only Latest Function Definition bcoz PVM performs Interpretation Process.
#VarirableLenArgsEx1.py
def disp(a,b,c,d,e): # Function Def-1
	print(a,b,c,d,e)
def disp(a,b,c,d): # Function Def-2
	print(a,b,c,d)
def disp(a,b,c): # Function Def-3
	print(a,b,c)
def disp(a,b): # Function Def-4
	print(a,b)
def disp(a): # Function Def-5
	print(a)

#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40) # Function Call-2 with 4 Args
disp(10,20,30) # Function Call-3 with 3 Args
disp(10,20) # Function Call-4 with 2 Args
disp(10) # Function Call-5 with 1 Arg

