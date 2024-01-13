#simple calculator
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def modulo(num1,num2):
    return num1%num2

#Take input from the user
num1=int(input("Enter first number"))
operation=input("What do you want to do(+,-,*,/,%):")
num2=int(input("Enter second number"))

result=0

if operation =="+":
    result=add(num1,num2)
    
elif operation =="-":
    result = sub(num1,num2)

elif operation == "*":
    result = mul(num1,num2)
elif operation == "/":
    result = div(num1,num2)
elif operation == "%":
    result = modulo(num1,num2)

else:
    print("please enter:+,-,*,/or%")
print(num1,operation,num2,'=',result)


