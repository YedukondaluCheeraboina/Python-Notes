#Program for accepting List of Numerical Values and get Squares and Square roots
# by  using map()
#MapEx3.py
print("Enter List of Numerical separated by space:")
vals=[float(val) for val in input().split() if float(val)>0]
print("Given Values")
print(vals) # [10,2,14,15,6]
#Find Squares
sqrs=list(map(lambda val:val**2, vals))
sqrts=tuple(map(lambda val:round(val**0.5,2),vals))
print("Squares List")
print(sqrs)
print("Square Roots")
print(sqrts)