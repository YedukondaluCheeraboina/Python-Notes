#SetCompEx1.py
s="APPLE IS RED in COLOUR"
vset={ ch    for ch in s   if ch.lower() in ['a','e','i','o','u']  }
print(vset,type(vset))