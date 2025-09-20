x=int(input("Enter the x value: "))
y=int(input("Enter the y value: "))

def pow(x,y):
    if y==0:
        return 1
    return x**(y-1)*x

print(pow(x,y))