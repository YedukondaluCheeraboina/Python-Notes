#NotTupleCompEx1.py
lst=[10,2,3,14,-4,15]
print(lst)
t=( val**2  for val in lst )
#Here t is an object of <class, 'generator'>
tpl=tuple(t)
print(tpl,type(tpl))
