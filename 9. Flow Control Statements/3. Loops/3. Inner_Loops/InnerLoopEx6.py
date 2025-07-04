#Program for Generating Mul Table for List of Random Values
#InnerLoopEx6.py
n=int(input("Enter How Many Values Mul Tables u Want:"))
if(n<=0):
    print("\t{} is invalid Input".format(n))
else:
    lst=[] #empty list-for adding values
    for i in range(1,n+1):
        value=int(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("Content of List")
        print(lst) # [10, 19, 0, 18, -6, 12]
        #Mul Code for random Numbers
        for num in lst: # outer loop
            if(num<=0):
                print("\t{} is Invalid Input".format(num))
            else:
                print("-"*50)
                print("Mul Table for :{}".format(num))
                print("-" * 50)
                for i in range(1,11): # inner loop
                    print("\t{} x {}={}".format(num,i,num*i))
                else:
                    print("-" * 50)



