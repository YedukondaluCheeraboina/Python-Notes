#Program for accepting List of Values and filter +ve and -ve separately.
#FilterEx1.py
def pos(val):
    if(val>0):
        return True
    else:
        return False
def neg(val):
    if(val<0):
        return True
    else:
        return False

#main program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
print("Given Values")
print(lst) # 10 20 -30 -40 -50 60 -70 -45
obj1=filter(pos,lst) # here obj1 is of type <class, 'filter'>
obj2=filter(neg,lst) # here obj2 is of type <class, 'filter'>
#Convert Filter Object into List / tuple / set object
pslist=list(obj1)
nglist=tuple(obj2)
print("List of +Ve Values=",pslist)
print("List of -Ve Values=",nglist)