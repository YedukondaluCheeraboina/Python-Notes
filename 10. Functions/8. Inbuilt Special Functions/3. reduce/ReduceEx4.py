#Program for Accepting List of words and get a Line of text
#ReduceEx4.py
import functools
print("Enter List of Words separated by Comma:")
vals=[val for val in input().split(",") ]
print("Given Words")
print(vals)
#vals=['Python', 'is', 'an', 'oop', 'lang', 'developed', ' by', 'Rossum']
line=functools.reduce(lambda k,v: k+" "+v,vals)
print("Line of Text")
print(line)
