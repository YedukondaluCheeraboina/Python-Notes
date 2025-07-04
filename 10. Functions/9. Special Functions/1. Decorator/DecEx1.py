#Program for Demonstarting Providing the additional Functionality to the Normal Function with decorators.
#DecEx1.py--Model-1
def  square(gv): # Decorator Definition--here gv is called Formal Parameter for Normal Function getval
	def  calcularesquare():
		n=gv() # Calling Normal Definition by using Formal parameter
		res=n**2
		return n,res
	return calcularesquare

def  getval():  # This Function Defined by KVR-Programmer
	return float(input("Enter Any Number:"))

#Main Program
cs=square(getval) # A Function Call Takes Normal Function Name as an Argument--Called Decorator
n,res=cs()
print("Square({})={}".format(n,res))