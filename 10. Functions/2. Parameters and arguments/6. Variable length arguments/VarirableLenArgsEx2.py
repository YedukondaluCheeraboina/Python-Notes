#Program for Demonstrating the need of Variable Length Arguments
#This Program will  execute as It is
#VarirableLenArgsEx2.py
def disp(a,b,c,d,e): # Function Def-1
	print(a,b,c,d,e)
disp(10,20,30,40,50) # Function Call-1 with 5 Args
#------------------------------------------------------------------------------------------
def disp(a,b,c,d): # Function Def-2
	print(a,b,c,d)
disp(10,20,30,40) # Function Call-2 with 4 Args
#------------------------------------------------------------------------------------------
def disp(a,b,c): # Function Def-3
	print(a,b,c)
disp(10,20,30) # Function Call-3 with 3 Args
#------------------------------------------------------------------------------------------
def disp(a,b): # Function Def-4
	print(a,b)
disp(10,20) # Function Call-4 with 2 Args
#------------------------------------------------------------------------------------------
def disp(a): # Function Def-5
	print(a)
disp(10) # Function Call-5 with 1 Arg
#------------------------------------------------------------------------------------------
