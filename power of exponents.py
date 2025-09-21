x=int(input("Enter the x value: "))
n=int(input("Enter the n value: "))

# 1.Using Recursion
def pow(x,n):
    if n==0:
        return 1
    return x**(n-1)*x

print(pow(x,n))

# 2. Divide and Conquer Rule
def power(x,n):
        # Base cases
    if n==0:
        return 1 
    elif x==0:
        return 0
        
    half= power(x,n//2)

    if n%2==0:
        return half*half
    else:
        return x* half*half

print(power(x,n))
        


