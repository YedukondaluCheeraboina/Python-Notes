#Program for accepting List of Old Salaries and Get New Salaries
# by giving 50% Hike by using map()
#MapEx2.py
print("Enter List of Old Salaries separated bu space:")
oldsal=[float(sal) for sal in input().split()]
print("Given Old Salaries")
print(oldsal)
newsal=list(map(lambda sal:sal+sal*50/100,oldsal))
print("Hiked Salaries")
print(newsal)
