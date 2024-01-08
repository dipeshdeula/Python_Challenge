#problem practice session

#Compute gravitaional force between two objects
# def gravitational_force(m1, m2, r):
#     G = 6.674 * (10 ** -11)   #Gravitational constant
#     F = G * ((m1 * m2) / (r ** 2))
#     return F
# m1=input("Enter the mass of first object:")
# m2=input("Enter the mass of second object:")
# r=input("Enter the distance between them:")
# F=gravitational_force(float(m1), float(m2), float(r))
# print("The Gravitational force between two objects is:",F)

#Ask user for input and calculate area of a triangle
# import math
# def area_of_triangle(a,b,c):
#     s=(a+b+c)/2
#     area=math.sqrt(s*((s-a)*(s-b)*(s-c)))
#     return area
# a=int(input("Enter length of side a:"))
# b=int(input("Enter length of side b:"))
# c=int(input("Enter length of side c:"))
# area=area_of_triangle(a,b,c)
# print("The area of traingle is:",area)

#For a given number,check whether the number is a prime number or not
# def prime_num(n):
#     if n/2 +1 ==False:
#         print("Number is not prime")
#     else:
#         print("Number is prime")
# num=int(input("Enter the number:"))
# prime_num(num)

#another solution

# def is_prime(num):
#     for i in range(2,num):
#         if(num%i==0):
#             return False
#     return True
# num=int(input("Enter the number to check : "))

# check_is_prime=is_prime(num)

# if check_is_prime:
#     print(f"{num} is a Prime Number.")
# else:
#     print(f"{num} is Not a Prime Number.")

#Ask the user to enter a number. Then find all the primes up to that number
# import math
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True
# number = int(input("Enter a number: "))
# print("Prime numbers up to ", number, " are: ")
# for num in range(2, number + 1):
#     if is_prime(num):
#         print(num)

#another method
# def is_prime(num):
#     for i in range(2,num):
#         if num % i==0:
#             return False
#     return True
# def all_primes(num):
#     primes=[]
#     for i in range(2,num+1):
#         if is_prime(i) is True:
#             primes.append(i)
#     return primes
# num=int(input("Enter the number:"))
# primes=all_primes(num)
# print(primes)


#Ask the user to enter a number. Then Find all the primes factors for the number
# def prime_factor(num):
#     divisor=2
#     factors=[]

#     while num>2:
#         if num%divisor==0:
#             factors.append(divisor)
#             num=num/divisor
#         else:
#             divisor+=1
#     return factors
# number=int(input("Enter a number:"))
# factors=prime_factor(number)
# print("The Prime numbers are",number)
# print("The prime Factors are",factors)

# #to find smallest prime factor
# print("The smallest prime factor are:",min(factors))

#strings in python
# A String is almost like a list. A list of Characters. you can access any element by index.
#you can run a fro loop on it . you will get each character as an element . Besides, you can
# also add two string or join two characters


# my_string="Hello world"

# print('Access is index')
# print('----------------')
# print(my_string[0])
# print(my_string[1])
# print(my_string[2])

# print('\nFro Loop')
# print('---------')
# for char in my_string :
#     print(char)

# String concatenation

# print('hello'+ 'world')

#Reverse String
# def reverse_string(str):
#     reverse=""
#     for char in str:
#         reverse=char+reverse
#     return reverse
# str=input("Enter your string:")
# result=reverse_string(str)
# print(result)

#Reverse String using stack
# def reverse_using_stack(str):
    #create an empty stack (list to use as stack)
    # stack=[]
    #push all character of string to stack
    # for char in str:
    #     stack.append(char)
        #pop all characters of string
        #and add it to the rev
#     rev=''
#     while len(stack):
#         last=stack.pop()
#         rev=rev+last
#        # print(last,rev)
#     return rev
# usr_str=input("Enter the string: ")
# reverse=reverse_using_stack(usr_str)
# print("Reversed String :",reverse)
        


#string slicing
# str="Hello young programmer"
# print(str[3:7])
# print(str[7:11])

# print('Skip range index')

# print(str[:11])
# print(str[3:])
# print(str[:])


#Reverse String using 

# def reverse_recur(str):
#     if len(str)==0:
#         return str
#     else:
#         return reverse_recur(str[1:]) + str[0]
# usr_str=input("Enter your String")
# rev_str=reverse_recur(usr_str)
# print("Reverse of your String:",rev_str)

#short-cut method for reverse string
txt="WELCOME TO LEARNING ZONE"
print(txt[::-1])

num="123"
print(num[::-1])

#reverse a number
def rev_number(num):
    rev=[]
    while num>0:
        rem=num%10
        rev.append(rem)
        num//=10
        
    reverse_number=''
    for num in rev:
        reverse_number=reverse_number+str(num)
    return reverse_number
usr_num=int(input("Enter Your Number: "))
reverse_number=rev_number(usr_num)
print("The reverse number is:",reverse_number)