#program for Demonstrating Inner loops
#InnerLoopEx1.py
for i in range(1,6): # Outer loop
    print("Outer Loop--Value of i={}".format(i))
    print("-"*50)
    for j in range(1,4): # inner loop
        print("\tInner Loop--Value of j={}".format(j))
    else:
        print("\tI am from else part of Inner Loop")
        print("-" * 50)
else:
    print("I am from else part of Outer Loop")
