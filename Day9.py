# practice session Day 2

# The problems sum of elements

# For a given list,get the sum of each number in list
# def get_sum(lst):
#     return sum(lst)
# print (get_sum([10,5,-3,7]))

#another approach
# sum=0
# nums=[1,2,3,4,5]
# for num in nums:
#     sum=sum+num
# print(sum)

#another shortcut
# nums=[2,3,4,5]
# total=sum(nums)
# print(total)

#Find the largest element of a list
# nums=[2,-1,8,44,80]
# max_num=max(nums)
# print("The maximum number from the list is:",max_num)

# def get_largest(num):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest
# nums=[2,-1,8,44,80]
# largest=get_largest(nums)
# print ("The largest number from the list is:",largest)

#Take a number as input. Then get the sum of the numbers. if the number is n. then get 0^2+1^2+3^2+....+n^2

# def get_sum_squre(num):
#     sum_square = 0
#     i = 1
#     while i <= num :
#         sum_square += i**2
#         i+=1
#     return sum_square
# num=int(input("Enter a positive number:"))
# print(get_sum_squre(num))

# def sumSq(num):
#     sum=0
#     for i in range(num+1):
#         sum=sum+pow(i,2)
#     return sum
# num=int(input("Enter a non-negative integer: "))
# print(sumSq(num))

#short cut using formula

# def sum_of_square(n):
#     sum=n*(n+1)*(2*n+1)/6
#     return sum
# num=int(input("Enter a non-negative integer: "))
# sum=sum_of_square(num)
# print("The sum of square is:",sum)

#For a list, Find the second largest number in the list

# def get_second_largest(num):
#     largest=nums[0]
#     second_largest = nums[0]
#     for i in range(1,len(nums)):
#         if nums[i] > largest:
#             second_largest = largest
#             largest=nums[i]
#         elif nums[i]>second_largest:
#             second_largest=nums[i]
#     return second_largest
# nums=[2,3,4,5,6,99,79]
# second_largest=get_second_largest(nums)
# print("Second highest number is:",second_largest)

#use max function to find second largest 
# nums=[2,3,4,5,70,7,80,9]
# nums.remove(max(nums))
# second_largest=max(nums)
# print("Second highest number is:",second_largest)
    
#Reverse Index
#python has a reverse way to acess indexes if you choose by using index -1 you will get the last element of the list
#And if you use -2 , you will get the second from ghe last element

# nums=[-1,2,3,5,99,100]
# print(nums[-1])
# print(nums[-2])
# print(nums[-3])

# nums=[5,7,8,9,23,4,5,0]
# nums.sort(reverse=True)
# print(nums[1])

# Find the second smallest element from the list
# nums=[-3,-2,-1,0,1,2,3,4,5]
# nums.remove(min(nums))
# second_smallest=min(nums)
# print("Second smallest element is:",second_smallest)

# def get_second_smallest(num):
    # smallest=nums[0]
    # second_smallest=nums[0]
    #infinity is considerd as larger than any amout, that's why 'smallest' and 'second_smallest' is assigned with infinity
#     smallest=float('inf')
#     second_smallest=float('inf')
#     for i in range(0,len(nums)):
#         if nums[i]<=smallest:
#             second_smallest=smallest
#             smallest=nums[i]
#         elif nums[i]<second_smallest:
#             second_smallest=nums[i]
#     return second_smallest
# second_smallest=get_second_smallest(nums)
# print("The second smallest element is",second_smallest)

# #alternative solution
# nums=[2,15,14,71,52,209,551]
# nums=sorted(nums)
# print(nums[1])

#Remove duplicate chars

#For a given string,remove all duplicate characters from that string
# def remove_duplicate_chars(string):
#     result=""
#     for char  in  string:
#         if char not in result:
#             result+=char
#     return result
# user_input=input("Enter your string:")
# no_duplicate  = remove_duplicate_chars(user_input)
# print('Without duplicate',no_duplicate)



#Conversion

#convert miles to kilometers
# def convert_miles_to_km(miles):
#     km=miles*1.60934
#     return km
# mile=int(input("Enter the number of miles you want to convert"))
# kilometers=convert_miles_to_km(mile)
# print(f"{mile} miles is equal to {kilometers} kilometers")

#convert celsius to Fahrenheit
# def convert_celsius_to_Fah(celsius):
#     celsius=(celsius*9/5)+32
#     return celsius
# fahrenheit=float(input("Enter temperature in Celsius :"))
# fahr=convert_celsius_to_Fah(fahrenheit)
# print(f"{fahrenheit} degree Celsius is equal to {fahr} degree F")