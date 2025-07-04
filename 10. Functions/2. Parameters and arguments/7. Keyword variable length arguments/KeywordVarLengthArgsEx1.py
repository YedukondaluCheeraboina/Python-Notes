#Program for Demonstrating the need of Key word Variable Length Arguments
#This Program will not execute as It is bcoz PVM Remebers Only Latest Function Definition bcoz PVM performs Interpretation Process.
#KeywordVarLengthArgsEx1.py
def disp(eno,ename,sal): #Function Def-1 
	print(eno,ename,sal)
def disp(tno,tname,sub1,sub2): #Function Def-2
	print(tno,tname,sub1,sub2)
def disp(sno,sname,hb1,hb2,hb3): #Function Def-3
	print(sno,sname,hb1,hb2,hb3)

#Main Program
disp(eno=10,ename="RS",sal=56) # Function Call-1 with 3 Keyword Args
disp(tno=20,tname="TR",sub1="Python",sub2="Java")# Function Call-2 with 4 Keyword Args
disp(sno=30,sname="SS",hb1="eating",hb2="Sleeping",hb3="Chating")# Function Call-3 with 5 Keyword Args