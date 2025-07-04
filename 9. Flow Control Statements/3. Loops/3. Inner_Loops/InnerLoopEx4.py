#program for Demonstrating Inner loops
#InnerLoopEx4.py
for i in range(5,0,-1): # Outer loop
    print("Outer Loop--Value of i={}".format(i))
    print("-"*50)
    j=1
    while(j<=3): # inner loop
        print("\tInner Loop--Value of j={}".format(j))
        j=j+1
    else:
        print("\tI am from else part of Inner Loop")
        print("-" * 50)
else:
    print("I am from else part of Outer Loop")
