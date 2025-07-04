#Program for Demonstrating the need of Key word Variable Length Arguments
#This Program will  execute as It is
#PureKeywordVarLengthArgsEx1.py
def disp(**k): # here **k is called Keyword Var length Parameter and whose type is dict
	print(k,type(k))


#Main Program
disp(eno=10,ename="RS",sal=56) # Function Call-1 with 3 Keyword Args
disp(tno=20,tname="TR",sub1="Python",sub2="Java")# Function Call-2 with 4 Keyword Args
disp(sno=30,sname="SS",hb1="eating",hb2="Sleeping",hb3="Chating")# Function Call-3 with 5 Keyword Args