#here we are checking if a number is prime or not

from sympy import isprime

def check_prime():
    try:
        num=int(input("enter a number:"))
        if isprime(num):
            print(f"the number {num} is prime")
        else:
            print(f"the number {num} is not prime")
    except ValueError:
        print("enter a valid number")

if __name__ == "__main__":
    check_prime()                   