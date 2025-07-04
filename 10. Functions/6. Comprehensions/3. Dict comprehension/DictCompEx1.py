#DictCompEx1.py
lst=[10,2,3,14,-4,15]
print(lst)
dobj={ val:val**2  for val in lst}
for k,v in dobj.items():
	print("\t{}-->{}".format(k,v))
