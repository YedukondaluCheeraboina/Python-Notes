#ListCompEx1.py
s="APPLE IS RED in COLOUR"
vlist=[ ch    for ch in s   if ch.lower() in ['a','e','i','o','u']  ]
print(vlist)