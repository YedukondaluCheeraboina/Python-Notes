#Program for accepting List of Values and filter +ve and -ve separately.
#FilterEx2.py
def pos(val):
    return (val>0)
def neg(val):
    return (val<0)

#main program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
print("Given Values")
print(lst) # 10 20 -30 -40 -50 60 -70 -45
pslist=list(filter(pos,lst))
nglist=tuple(filter(neg,lst))
print("List of +Ve Values=",pslist)
print("List of -Ve Values=",nglist)