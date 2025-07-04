#Program for accepting List of Values and filter +ve and -ve separately.
#FilterEx4.py
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
print("Given Values")
print(lst) # 10 20 -30 -40 -50 60 -70 -45
pslist=list(filter(lambda val: val>0,lst))
nglist=tuple(filter(lambda val: val<0,lst))
print("List of +Ve Values=",pslist)
print("List of -Ve Values=",nglist)