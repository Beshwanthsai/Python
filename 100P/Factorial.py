#here we are performing factorial of a number in python

# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result=result*i
#     return result

# n=int(input("Enter the number: "))
# print("The factorial of",n,"is",factorial(n))


# reccursicve method

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("enter the number: "))
factorial(n)
print("The factorial of",n,"is",factorial(n))