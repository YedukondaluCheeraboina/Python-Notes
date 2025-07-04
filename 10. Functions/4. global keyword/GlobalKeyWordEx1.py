#Program for Demonstrating the need of global keyword
#GlobalKeyWordEx1.py
def increment():
	global a # refers the value of global var 'a'
	a=a+1

def modify1():
	global a
	a=a*2

#Main Program
a=10  # here a is called global variable
print("Main Program: Value of a before increment=",a) # 10
increment()
print("Main Program: Value of a after increment=",a) # 11
modify1()
print("Main Program: Value of a after modify1()=",a) # 22




