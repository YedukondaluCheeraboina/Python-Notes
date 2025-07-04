#Program for Demonstarting Providing the additional Functionality to the Normal Function without decorators.
#Non-DecEx1.py
def  getval():  # This Function Defined by KVR-Programmer
	return 5

def square():						#Udaya is asking, Sir Give Square of 5
	n=getval()
	res=n**2
	print("Square({})={}".format(n,res))

def squareroot():				#Swati is asking, Sir Give Square Root of 5
	n=getval()
	res=n**0.5
	print("SquareRoot({})={}".format(n,res))

def cube():						    #Lakshmi is asking, Sir Give Cube of 5
	n=getval()
	res=n**3
	print("Cube({})={}".format(n,res))

#Main Program
square()
squareroot()
cube()

