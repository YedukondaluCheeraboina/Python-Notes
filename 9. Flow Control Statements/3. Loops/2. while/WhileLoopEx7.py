#Program for Finding sum of First N Natural Numbers,
# also find Sum of Square and Sum of Cubes First N Natural Numbers.
#WhileLoopEx7.py
n=int(input("Enter How Natural Nums U want to Find:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Nat Nums\t\tSquares\t\t\tCubes")
    s,ss,cs=0,0,0 # Additive Identity--Keeps Track of repeated sum
    print("-" * 50)
    i=1
    while(i<(n+1)):
        print("\t{}\t\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("-"*50)
        print("\t{}\t\t\t\t{}\t\t\t{}".format(s,ss,cs))
        print("-" * 50)