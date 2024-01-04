# #for loop 
# basket = ['apple','banana','strawberry','grapes','mango']
# fruit=basket.sort()

# for fruit in basket:
#     print(fruit)

# #condition in for loop
# num=[1,2,3,-1,4,5,6,7]

# for nums in num:
#     if(nums>5):
#         print(nums)

# #break in l00p 
# for num1 in num:
#     if(num1<0):
#         break
#     print(num1)

# #continue keyword helps to skip some element from the list
#     num2=[1,2,3,4,5,6,7,8,9,10]
#     for i in num2:
#         if(i==5 or i==7):
#             continue
#         print(i)
# #break will stop immediately . Continue will skip the current iteration
# #continue will skip the rest part of the current iteration

#The range() function can take up to three parameters:range(start,stop,step)
for n in range(1,5,6):
    print(n)

#range(stop)
for n in range(3):
    print(n)