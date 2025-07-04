#Program for Demonstarting Providing the additional Functionality to the Normal Function with decorators.
#DecEx2.py--Model-2
def  square(gv): # Decorator Definition--here gv is called Formal Parameter for Normal Function getval
	def  calcularesquare():
		n=gv() # Calling Normal Definition by using Formal parameter
		res=n**2
		return n,res
	return calcularesquare

@square  # Nothing but  square(getval)
def  getval():  # This Function Defined by KVR-Programmer
	return float(input("Enter Any Number:"))

#Main Program
n,res=getval() # Normal Function Call
print("square({})={}".format(n,res))