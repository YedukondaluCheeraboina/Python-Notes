#Program for Demonstrating the need of Variable Length Arguments
#This Program will  execute as It is
#PureVarirableLenArgsEx2.py
def  disp( *k): # here *k is called Variable Length Parameter and whose type is tuple
	if(len(k)==0):
		print("\tempty")
	else:
		for val in k:
			print("\t{}".format(val),end=" ")
		print()

#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40) # Function Call-2 with 4 Args
disp(10,20,30) # Function Call-3 with 3 Args
disp(10,20) # Function Call-4 with 2 Args
disp(10) # Function Call-5 with 1 Arg
disp() # Function Call-6 with 0 Arg
