#Program for Demonstrating Posstional Arguments
#PossArgsEx1.py
def dispstudinfo(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))


#Main Program
print("-"*50)
print("\tSTNO\tNAME\tMARKS")
print("-"*50)
dispstudinfo(10,"RS",45.67) # Function Call with 3 Pos Args
dispstudinfo(20,"TR",45.89)  # Function Call with 3 Pos Args
dispstudinfo(30,"DR",65.29)  # Function Call with 3 Pos Args
dispstudinfo(40,"JH",56.78)  # Function Call with 3 Pos Args
print("-"*50)