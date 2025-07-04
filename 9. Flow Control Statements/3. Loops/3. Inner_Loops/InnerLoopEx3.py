#program for Demonstrating Inner loops
#InnerLoopEx3.py
i=1
while(i<=5): # Outer loop
    print("Outer Loop--Value of i={}".format(i))
    print("-"*50)
    for j in range(3,0,-1): # inner loop
        print("\tInner Loop--Value of j={}".format(j))
    else:
        i=i+1
        print("\tI am from else part of Inner Loop")
        print("-" * 50)
else:
    print("I am from else part of Outer Loop")
