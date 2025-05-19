#here we are finding largets of 3 numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
def LOT(a,b,c):
    if(a>b and a>c):
        print("a is largest")
    elif(b>a and b>c):
        print("b is largest")
    else:
        print("c is largest")

LOT(a,b,c)


#typecasting

cgpa = 9.78

print(type(cgpa))
print(cgpa)
typecasted_cgpa = int(cgpa)
print(type(typecasted_cgpa))
print(typecasted_cgpa)
#typecasting