#Program for accepting List of Old Salaries and Get New Salaries
# by giving 50% Hike by using map()
#MapEx1.py
def hike(sal):
    return(sal+sal*50/100)


#Main Program
print("Enter List of Old Salaries separated bu space:")
oldsal=[float(sal) for sal in input().split()]
print("Given Old Salaries")
print(oldsal)
mapobj=map(hike,oldsal)  # here mapobj is an object <class, map>
#Convert Map object into List object
newsal=list(mapobj)
print("Hiked Salaries")
print(newsal)
