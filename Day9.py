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

def get_second_largest(num):
    largest=nums[0]
    second_largest = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest=nums[i]
        elif nums[i]>second_largest:
            second_largest=nums[i]
    return second_largest
nums=[2,3,4,5,6,99,79]
second_largest=get_second_largest(nums)
print("Second highest number is:",second_largest)
    