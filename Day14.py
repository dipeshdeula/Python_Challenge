#simple calculator
# def add(num1,num2):
#     return num1+num2

# def sub(num1,num2):
#     return num1-num2

# def mul(num1,num2):
#     return num1*num2

# def div(num1,num2):
#     return num1/num2

# def modulo(num1,num2):
#     return num1%num2

# #Take input from the user
# num1=int(input("Enter first number:"))
# operation=input("What do you want to do(+,-,*,/,%):")
# num2=int(input("Enter second number:"))

# result=0

# if operation =="+":
#     result=add(num1,num2)
    
# elif operation =="-":
#     result = sub(num1,num2)

# elif operation == "*":
#     result = mul(num1,num2)
# elif operation == "/":
#     result = div(num1,num2)
# elif operation == "%":
#     result = modulo(num1,num2)

# else:
#     print("please enter:+,-,*,/or%")
# print(num1,operation,num2,'=',result)


#password generator

#Generate a password. your password may contain letters in uppercase or lowercase. it also may contain digits or special characters
#To select a random character from a string . you can import random . Then use the random choice method.
#This will select a character from the provided string.

#Also , you can import the string module. 

#This is not just the string type variable. Instead, it has a lot of extra functionalities

#for example, you can use string.ascii_letters to get all the characters a to z both in lowercase and uppercase.
#Similarly, you can use string.digits to get all the single digits. Also, you can use string.punctuation to get all the special characters

# import string
# print("All letters")
# alpha=string.ascii_letters
# lenAlpha=len(alpha)
# for char in (alpha):
#     print(char)

# print('all digits')
# print(string.digits)

# print('all special characters')
# print(string.punctuation)


#password generator code

# import string
# import random

# def generate_password(size):
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     password=""
#     for char in range(size):
#         rand_char = random.choice(all_chars)
#         password = password + rand_char
#     return password

# pass_len = int(input("How many characters your password?"))
# new_password = generate_password(pass_len)
# print("Your new password:",new_password)

#Gmail and password generator

import random
import string

first=input("Enter your first name:")
last=input("Enter your last name:")
num=int(input("Enter your password length:"))

all_chars = string.ascii_letters + string.digits + string.punctuation

email = first + '.' + last + '@gmail.com'
password=""

for i in range(num):
    rand_char = random.choice(all_chars)
    password = password + rand_char

print("your Gmail Id:"+email)
print("your password:"+ password)