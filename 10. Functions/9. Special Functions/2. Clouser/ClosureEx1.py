#Program for Demonstrating the Concept of Closures
#ClosureEx1.py
def fun1(a):
	print("I am from Outer Function Body:")
	def fun2(b): # Here fun2 is Called Closure to fun1()
			print("\tI am from Inner Function Body:")
			print("\tOuter Fun val={} and Inner Val={}".format(a,b))
	return fun2

#main program
fn2=fun1(10) # Outer Function Call--Called and Executed
fn2(100) # Inner Function of Outer Function
fn2(200) # Inner Function of Outer Function
fn2(300) # Inner Function of Outer Function
