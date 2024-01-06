#return the sum of all the divisor of a number,
#without including it. A divisor that divides into 
#another withour a remainder

# def sum_divisor(n):
#     #Return the sum of all the divisior of n, not including n
#     if(n==0):
#         return 0
#     sum=0
#     divisor=1
    
#     while divisor <=n //2:
#         #check if divisor is a divisor of n
#         if n% divisor ==0:
#             sum=sum+divisor
#         divisor+=1
#     return sum

# print(sum_divisor(0))
# print(sum_divisor(3))

#problem : 2 
#The multiplication_table function prints the result of a number passed 
#to it multiplied by 1 throug 5 . An additional requirement is that the result
#is not to excedd 25, which is done with the break statement

def multiplication_table(number):
    multipler=1
    while multipler <=5:
        result=number*multipler
        if result>=25:
            break
     
        print(f"{number} x {multipler} = {result}")
        multipler +=1

multiplication_table(3)
multiplication_table(5)
