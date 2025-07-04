#Program for Demonstrating the need of globals()
#In This Program Local and global Variable Names are Same
#GlobalsFunEx1.py
a=10
b=20  # Here 'a' , 'b'  are called global variables
def operation():
	dobj=globals() # Here dobj is an object of <class,'dict'>
	print("-"*50)
	print("Both Programmer and invisible global Variables")
	print("-"*50)
	for gvn,gvv in dobj.items():
		print("{}--->{}".format(gvn,gvv))
	print("-"*50)
	print("\tProgrammer global Variables-way-1")
	print("-"*50)
	print("\t Global Var a={}".format(dobj.get('a')))
	print("\t Global Var b={}".format(dobj.get('b')))
	print("-"*50)
	print("\tProgrammer global Variables-way-2")
	print("-"*50)
	print("\t Global Var a={}".format(dobj['a']))
	print("\t Global Var b={}".format(dobj['b']))
	print("-"*50)
	print("\tProgrammer global Variables-way-3")
	print("-"*50)
	print("\t Global Var a={}".format(globals()['a']))
	print("\t Global Var b={}".format(globals()['b']))
	print("-"*50)
	print("\tProgrammer global Variables-way-4")
	print("-"*50)
	print("\t Global Var a={}".format(globals().get('a')))
	print("\t Global Var b={}".format(globals().get('b')))
	print("-"*50)

#main Program
operation()
