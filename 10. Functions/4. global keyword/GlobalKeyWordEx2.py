#Program for Demonstrating the need of global keyword
#GlobalKeyWordEx2.py
def increment():
	global a,b
	a=a+1
	b=b+1

def modify1():
	global a,b
	a=a*2
	b=b*2

#Main Program
a,b=10,20  # here a and b is called global variable
print("Main Program-before increment() Value of a ={} and b={}".format(a,b)) # a=10 b=20
increment()
print("Main Program-after increment() Value of a ={} and b={}".format(a,b)) # a=11 b=21
modify1()
print("Main Program-after modify1() Value of a ={} and b={}".format(a,b)) # a=22 b=42




