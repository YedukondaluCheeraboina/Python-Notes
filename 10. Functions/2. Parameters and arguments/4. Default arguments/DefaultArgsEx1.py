#Program for Demonstrating Default Arguments
#DefaultArgsEx1.py
def dispstudinfo(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("-"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudinfo(10,"RS",45.67) # Function Call with 3 Pos Args
dispstudinfo(20,"TR",45.89)  # Function Call with 3 Pos Args
dispstudinfo(30,"DR",65.29)  # Function Call with 3 Pos Args
dispstudinfo(40,"JH",56.78)  # Function Call with 3 Pos Args
print("-"*50)