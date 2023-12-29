#whil loop
# count=0
# sum=0
# while count<5:
#     sum=sum+count
#     print(sum)
#     count+=1
# print("The sum of count value is :"+str(sum))

#Conceptual: while loop Structure
# 1. Declare a loop variable
# 2. Write the while keyword
# 3. Add a stopping condition after the while.
# 4. Underneath while, write the repeating work.
# 5. Update the loop variable
# If the condition becomes True,the loop will continue. If the condition becomes False the loop will stop running.

# count =5
# while count>0:
#     print(count)
#     count=count-1

#sum of number

# i=0
# sum=0
# while i<10:
#     sum=sum+i
#     print(sum)
#     i=i+1
# print("The sum of 10 number is :"+str(sum))

#display only even number
# i=0
# even_sum=0
# while i<20:
#     if(i%2==0):
#         even_sum=even_sum+i
#         print(even_sum)
#     i=i+1
        
# print("The sum of all even number between  0-20 is :"+str(even_sum))

#display odd number
i=0
odd_sum=0
while i<=19:
    if(i%2 != 0):
        odd_sum += i
        print(odd_sum)
    i+=1
print("The sum of all odd number between 0 -20:"+str(odd_sum))