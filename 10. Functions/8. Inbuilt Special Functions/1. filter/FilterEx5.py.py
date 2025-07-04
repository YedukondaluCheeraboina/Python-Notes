#Program for Accepting List of Values and Filter Prime Numbers
#FilterEx5.py
def isprime(val):
    res=True
    for i in range(2,val):
        if(val%i==0):
            res=False
            break
    return res

#Main Program
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split() if int(val)>=2]
print("Given Values")
print(lst)
primes=list(filter(isprime,lst))
print("List of Primes")
print(primes)



