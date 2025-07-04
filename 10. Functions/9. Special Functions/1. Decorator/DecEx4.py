#Program for Demonstarting Providing the additional Functionality to the Normal Function with decorators.
#DecEx4.py
def cube(calsqrt):
	def calculatecube():
		n,sqv,sqrtval=calsqrt()
		cbtval=n**3
		return n,sqv,sqrtval,cbtval
	return calculatecube

def squareroot(calsq):
	def calculatesquareroot():
		n,sqv=calsq()
		sqrtval=n**0.5
		return n,sqv,sqrtval
	return calculatesquareroot

def  square(gv): # Decorator Definition--here gv is called Formal Parameter for Normal Function getval
	def  calculatesquare():
		n=gv() # Calling Normal Definition by using Formal parameter
		res=n**2
		return n,res
	return calculatesquare

@cube
@squareroot   # Nothing but  squareroot(square(getval))
@square  # Nothing but  square(getval)
def  getval():  # This Function Defined by KVR-Programmer
	return float(input("Enter Any Number:"))

#Main Program
n,sqv,sqrtval,cbtval=getval() # Normal Function Call
print("square({})={}".format(n,sqv))
print("squareroot({})={}".format(n,sqrtval))
print("Cube({})={}".format(n,cbtval))