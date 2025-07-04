#program for Demonstrating Inner loops
#InnerLoopEx2.py
i=5
while(i>=1): # Outer loop
    print("Outer Loop--Value of i={}".format(i))
    print("-"*50)
    j=3
    while(j>=1): # inner loop
        print("\tInner Loop--Value of j={}".format(j))
        j=j-1
    else:
        i=i-1
        print("\tI am from else part of Inner Loop")
        print("-" * 50)
else:
    print("I am from else part of Outer Loop")
