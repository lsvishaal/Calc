
def InputNumbers():
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
    return a,b

def Addition(a,b):
    return a+b

def Subtraction(a,b):
   return a-b

def Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b

num1,num2=InputNumbers()
print(f"You entered : {num1} and {num2}")
print(f"Addition: {Addition(num1,num2)}")
print(f"Subtraction: {Subtraction(num1,num2)}")
print(f"Multiplication :{Multiplication(num1,num2)}")
print(f"Division:{Division(num1,num2)}")