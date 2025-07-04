#Program for Demonstrating the need of globals()
#In This Program Local and global Variable Names are Different
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # Here 'a' , 'b' , 'c' and 'd' are called global variables
def operation():
	x=100
	y=200
	z=300
	k=400 # here x,y,z and k are called Local variables
	res=x+y+z+k+a+b+c+d
	print("result=",res)

#main Program
operation()
