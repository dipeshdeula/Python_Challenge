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
