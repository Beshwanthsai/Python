def my_fun():
    print("my name is beshwanth sai katari")
my_fun()

def my_name(name):
    print(f"my name is {name}")

my_name("Beshwanth Sai Katari")

def add(a,b):
    return a+b

result = add(1,2)
print(result)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

re = fib(3)
print(re)



def user_dict(firstname,lastname,age):
    user_info = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return user_info

sol = user_dict(firstname="beshwanthsai", lastname="katari", age='21')
print(sol)