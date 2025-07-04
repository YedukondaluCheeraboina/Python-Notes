#Program for Demonstrating Posstional Arguments
#PossArgsEx2.py
def dispstudinfo(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("-"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
dispstudinfo(10,"RS",45.67,"PYTHON") # Function Call with 4 Pos Args
dispstudinfo(20,"TR",45.89,"PYTHON")  # Function Call with 4 Pos Args
dispstudinfo(30,"DR",65.29,"PYTHON")  # Function Call with 4 Pos Args
dispstudinfo(40,"JH",56.78,"PYTHON")  # Function Call with 4 Pos Args
print("-"*50)