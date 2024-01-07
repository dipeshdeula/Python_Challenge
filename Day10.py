#convert a decimal number to binary number
# def decimal_to_binary(num):
#     data=[]
#     while num>0:
#         rem = num % 2
#         data.append(rem)
#         num //= 2
#     data.reverse()

#     binary = ''
#     for bit in data:
#         binary += str(bit)
#     return binary
# num=int(input("Enter decimal number:"))
# binary=decimal_to_binary(num)
# print(f"Binary conversion of {num} is :{binary}")



#convert a binary to decimal number
# def binary_to_decimal(num):
#     binary = list(map(int,list(num)))
#     power = len(binary)-1
#     dec_val = 0
#     for i in range(len(binary)):
#         dec_val += binary[i]*(2**power)
#         power -= 1
#     return dec_val
# num=input("Enter Binary Number:")
# decimal=binary_to_decimal(num)
# print(f"Decimal Conversion of {num} is:{decimal}")
#convert a decimal number to binary number using a recursive function
# def dec_to_binary(n):
#     if n>1:
#         dec_to_binary(n//2)
#     print(n%2,end='')

# #decimal number
# num=int(input("Enter decimal number:"))
# dec_to_binary(num)
# print(" ")

#convert a binary number to decimal number using a recursive function


#simple intrest problem

#you borrowed $5000 for 2 years with 2% interest per year
#Calculate the simple interest to know how much you have to pay?
# def calc_interest():
#     p = int(input('Enter Principal amount:'))
#     t = int(input('Enter Time period:'))
#     r = float(input('Enter Rate of Interest:(in percentage)'))/100

#     #formula to calculate simple interest
#     SI = (p*t*r)/100
#     print(f'The Simple Interest is :${SI:.2f}')
# calc_interest()

#calculate compound interest
# def cal_comopound_interest():
#     P = float(input('Enter the principal amount:'))
#     T = float(input('Enter the time period:'))
#     R = float(input('Enter the rate of interest:(in percentage)'))/100
#     N = int(input('Enter the number of times interest is paid per year:'))
#     #Formula to calculate compound interest
#     A=P * pow((1+ (R/N)),N*T)
#     CI=(A-P)
#     print(f'The Compound Interest is ${CI:.2f}')
# cal_comopound_interest()

#Calculate grade of five subjects
def calculateGrade():
    print('Enter your marks of each subject')
    sub1=int(input("first subject:"))
    sub2=int(input("second subject:"))
    sub3=int(input("Third subject:"))
    sub4=int(input("fourth subject:"))
    sub5=int(input("fifth subject:"))

    avg=(sub1+sub2+sub3+sub4+sub5)/5

    if avg>=90:
        print("Your Grade is A")
    elif avg>=80:
        print("Your Grade is B")
    elif avg>=70:
        print("Your Grade is C")
    elif avg>=60:
        print("Your Grade is D")
    else:
        print("Your Grade is F")
calculateGrade()
       
