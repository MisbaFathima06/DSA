# 1. Using Loop
num=int(input("Enter a number to find the factorial: "))

def factorial(nums):
    result=1
    for i in range(1,nums+1):
        result=result*i
    return result
print(factorial(nums=num))

# 2. Using Recursion
def factorials(n):
    if n==0 or n==1:        #Base case
        return 1
    return n*factorials(n-1)
print(factorials(n=num))