#Program for Demonstrating the need of Variable Length Arguments
#This Program will  execute as It is
#PureVarirableLenArgsEx3.py
def  disp( sno,sname,*k): # here *k is called Variable Length Parameter and whose type is tuple
	print("-"*50)
	print("Student Number={}".format(sno))
	print("Student Name={}".format(sname))
	s=0
	for val in k:
		print("\t{}".format(val),end=" ")
		s=s+val
	print("\n\tsum={}".format(s))
	print("-"*50)
#Main Program
disp(100,"Krishna",10,20,30,40,50) # Function Call-1 with 5 Args
disp(200,"Rahman",10,20,30,40) # Function Call-2 with 4 Args
disp(300,"Amit",10,20,30) # Function Call-3 with 3 Args
disp(400,"Naresh",10,20) # Function Call-4 with 2 Args
disp(500,"Vastava",10) # Function Call-5 with 1 Arg
disp(600,"Sai") # Function Call-6 with 0 Arg
