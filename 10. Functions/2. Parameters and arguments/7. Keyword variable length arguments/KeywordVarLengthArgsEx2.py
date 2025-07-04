#Program for Demonstrating the need of Key word Variable Length Arguments
#This Program will execute as It is
#KeywordVarLengthArgsEx2.py
def disp(eno,ename,sal): #Function Def-1 
	print(eno,ename,sal)
disp(eno=10,ename="RS",sal=56) # Function Call-1 with 3 Keyword Args
#----------------------------------------------------------------------------------
def disp(tno,tname,sub1,sub2): #Function Def-2
	print(tno,tname,sub1,sub2)
disp(tno=20,tname="TR",sub1="Python",sub2="Java")# Function Call-2 with 4 Keyword Args
#----------------------------------------------------------------------------------
def disp(sno,sname,hb1,hb2,hb3): #Function Def-3
	print(sno,sname,hb1,hb2,hb3)
disp(sno=30,sname="SS",hb1="eating",hb2="Sleeping",hb3="Chating")# Function Call-3 with 5 Keyword Args
#----------------------------------------------------------------------------------


