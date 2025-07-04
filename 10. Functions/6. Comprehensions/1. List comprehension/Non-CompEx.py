#Non-CompEx.py
s="Apple is red"
vlist=[]
for ch in s:
	if(ch.lower() in['a','e','i','o','u']):
		vlist.append(ch)
print(vlist)
