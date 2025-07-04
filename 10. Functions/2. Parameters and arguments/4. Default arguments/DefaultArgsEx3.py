#Program for Demonstrating Default Arguments
#DefaultArgsEx3.py
def dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#Main Program
print("-"*50)
print("\tSTNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("-"*50)
dispstudinfo(10,"RS",45.67) # Function Call with 3 Pos Args
dispstudinfo(20,"TR",45.89)  # Function Call with 3 Pos Args
dispstudinfo(30,"DR",65.29)  # Function Call with 3 Pos Args
dispstudinfo(40,"JH",56.78)  # Function Call with 3 Pos Args
dispstudinfo(50,"DT",11.11,cnt="USA",crs="Politics") # Function Call with 4 Pos Args
dispstudinfo(60,"PT",21.11,cnt="RSA") # Function Call with 4 Pos Args
#dispstudinfo(marks=56.22,sno=70,crs="C",sname="KM")
print("-"*50)