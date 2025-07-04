#Program for Demonstrating the need of Key word Variable Length Arguments
#This Program will  execute as It is
#PureKeywordVarLengthArgsEx3.py
def findtotalmarks(sno,sname,cls,**submarks):
	print("="*50)
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Student Class:{}".format(cls))
	print("-"*50)
	totmarks=0
	for subject,marks in submarks.items():
		print("\t{}---->{}".format(subject,marks))
		totmarks=totmarks+marks
	print("\tTOTAL MARKS={}".format(totmarks))
	print("="*50)




#Main Program
findtotalmarks(10,"Krishna","X",English=70,Hindi=80,Telugu=60,Maths=90,Science=90,Social=85)
findtotalmarks(20,"Pariskheet","XII",Eng=85,Sanskrit=99,Maths=75,Phy=60,Che=58)
findtotalmarks(30,"Rajesh","B.Tech(CSE)",OS=50,DBMS=60,NW=50)
findtotalmarks(40,"Rossum","Research")


