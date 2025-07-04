#Program for Demonstrating the need of globals()
#In This Program Local and global Variable Names are Same
#GlobalsFunEx3.py
a=10
b=20
c=30
d=40 # Here 'a' , 'b' , 'c' and 'd' are called global variables
def operation():
	a=100
	b=200
	c=300
	d=400 # Here 'a' , 'b' , 'c' and 'd' are called  Local variables
	res=a+b+c+d+globals()['a']+globals().get('b')+globals()['c']+globals().get('d')
	print("result=",res)

#main Program
operation()
