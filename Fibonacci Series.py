n=int(input("Enter the number you want to find the fibo series of: "))

# 1. Using Recursion
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

print("Recursive:", fibo(n))

# 2. Memoization

def fib(n):
    memo={0:0,1:1}      # base cases stored in dictionary

    #function  for func calls
    def function(x):
        if x in memo:
            return memo[x]
        else:
            memo[x]=function(x-1)+function(x-2)
            return memo[x]
    return function(n)       # this return is for the outer function

print(fib(n))