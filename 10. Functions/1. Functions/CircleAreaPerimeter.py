#CircleAreaPerimeter.py
#Functions for cal area and Perimeter
def circlearea():
    r=float(input("Enter Radius for Cal area of Circle:"))
    if(r<=0):
        return("\t{} is Invalid input".format(r))
    else:
        ac=3.14*r**2
        return("Area of Circle={}".format(ac))
def circleperi():
    r = float(input("Enter Radius for Cal Perimeter of Circle:"))
    if (r <= 0):
        print("\t{} is Invalid input".format(r))
    else:
        pc = 2*3.14 * r
        print("Perimeter of Circle={}".format(pc))
#main Program
res=circlearea()
print(res)
print("---------------------------")
circleperi()