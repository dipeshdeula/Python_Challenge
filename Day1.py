#Review some basic
#print("Lets complete this challenge")

#creating a function

# def calculate_area(radius):
#     pi=3.614
#     area=pi*(radius**2)
#     return area

# area_Circle=calculate_area(3)
# print("The area of circle is :"+ str(area_Circle))

# #function for calculating area of triangle
# def calculate_triangle(base,height):
#     area=(base*height)/2
#     return area
# area_triangle=calculate_triangle(2,3)
# print("The area of triangle is :"+str(area_triangle))


#string in python
# name="Dipesh"
# print(name)

# #boolean

# is_Cold=False
# print(is_Cold)

# name="dipesh"
# print(type(name))

# security='Tom hanks'
# security='Tom cruise'
# Security='Tom hardy'
# print(security)

#user input in variable
#By default user input is taken as as string. when the user insert text or 
# a number, both are taken as a string

# input("Tell me you favourite food:")

# name=input("who is your dream girl:")
# print("Dream girl"+name)

#if you expect a number, use special keyword int or float to convert user input to a number
# siblings_text=input("numbers of siblings you have:")
# siblings=int(siblings_text)
# print(siblings)

#modulo helps to know remainder value
# print(19%2)

# The is_positive function should return True if the number received is positive, otherwise it returns None.
# Can you fill in the gaps to make that happen?

# def is_positive(number):
#     if(number>0):
#         return True
    
# a=is_positive(3)
# print(a)

# def user_name(name):
#     if(len(name)>5):
#         return "Your name is long."
#     else:
#         return "poor name"
    

# namm=user_name("Dipesh")
# print(namm)

# name1=user_name("dev")
# print(name1)

#valid user credential in python concept of using if -else + operators and functions
# def user_auth(username,passowrd):
#     if(username =="Dipesh@123" and passowrd=="devjava@123"):
#         return "Welcome Dipesh"
#     else:
#         return "Invalid UserName and Password"

# verificationUser=input("user name:")
# verificationPass=input("Valid pass:")
# print(user_auth((verificationUser),(verificationPass)))

# def is_even(number):
#     if(number % 2 ==0):
#         return True
#     else:
#         return False

# def numType(number1):
#     if(number1>0):
#         return " this is postive number"
#     else:
#         return "This is negative number"
    
# num = input("enter the number : ")
# print(is_even(int(num)))
# print(numType(int(num)))

#elif statement in py
#elif is the else if statement

# def StudentIdentification(name,roll,year):
#     if(name=="hsm"):
#         return "student of hsm"
#     elif(roll==9):
#         return "roll 9 student only"
#     elif(year==2018):
#         return "2018 batch only "
#     else:
#         return "Not a valid student"
# inputname=input("name of student:")
# intputroll=input("roll of student:")
# inputyear=input("year of the student:")

# print(StudentIdentification(inputname,int(intputroll),int(inputyear)))


# Question 5
# If a filesystem has a block size of 4096 bytes, this means that a file comprised 
# of only one byte will still use 4096 bytes of storage. A file made up of 4097 
# bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill 
# in the gaps in the calculate_storage function below,
# which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size=4096
    blocks_needed=(filesize + (block_size - 1)) // block_size
    storage_required=blocks_needed * block_size
    return storage_required
print(calculate_storage(6000))

# def calculate_storage1(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks=block_size//filesize
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder =full_blocks%block_size
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder < 0:
#         return full_blocks*block_size
    
# print(calculate_storage1(1))
