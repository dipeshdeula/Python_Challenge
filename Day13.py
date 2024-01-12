# #simple Digital Clock
# x=5
# def double_global_x(x):
#     x=2*x;
#     return x
# print('use globla keyword')
# result=double_global_x(x)
# print(result)
# print('Updated value of X:',x)

# number=1
# while number<=7:
#     print(number,end=" ")
#     number+=1


#complete the function digits(n) that returns how many digits the number has.
#for example: 25 has 2 digits and 144 has 3 digits. 
#hint : you can figure it out the digits a number by dividign it by 10 once per digit until there are no digits left

# def digits(n):
#     count=0
#     if n==0:
#         return 1
#     while n>0:
#         count+=1
#         n=n//10
#     return count
# print(digits(25))
# print(digits(144))
# print(digits(1000))
# print(digits(0))

# This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

# 1 2 3 

# 2 4 6 

# 3 6 9

# def multiplication_table(start, stop):
# 	for x in range(1,stop+1):
# 		for y in range(start,start+stop):
# 			print(str(x*y), end=" ")

# 		print()

# multiplication_table(1, 3)

# for x in range(1, 10, 3):
#     print(x)

# for x in range(10):
#     for y in range(x):
#         print(y,end=' ')
#         print()

# The counter function counts down from start to stop when start is bigger than stop, and counts up from 
# start to stop otherwise. Fill in the blanks to make this work correctly.

# def counter(start, stop):
#     x = start
#     if start > stop:
#         return_string = "Counting down: "
#         while x >= stop:
#             return_string += str(x)
#             if x > stop:
#                 return_string += ","
#             x -= 1
#     else:
#         return_string = "Counting up: "
#         while x <= stop:
#             return_string += str(x)
#             if x < stop:
#                 return_string += ","
#             x += 1
#     return return_string
# print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1))   # Should be "Counting down: 2,1"
# print(counter(5, 5))   # Should be "Counting up: 5"

# def even_numbers(maximum):
#     return_string = ""
#     for x in range(2, maximum + 1, 2):
#         return_string += str(x) + " "
#     return return_string.strip()

# # Test cases
# print(even_numbers(6))   # Should be 2 4 6
# print(even_numbers(10))  # Should be 2 4 6 8 10
# print(even_numbers(1))   # No numbers displayed
# print(even_numbers(3))   # Should be 2
# print(even_numbers(0))   # No numbers displayed

# def votes(params):
# 	for vote in params:
# 	    print("Possible option:" + vote)

# def decade_counter():
# 	while year < 50:
# 		year += 10
# 	return year
        
# def find_x_positions(words):
#     for index, char in enumerate(words):
#         if char == 'x':
#             print(index)

# find_x_positions("supercalifragilisticexpialidocious")

# message=" 9 like you"
# print(message[0])
# # message[0]="I"
# print(message)

#string is immuatable

#string split
# name="my name is dipesh"
# name_split=name.split()
# print(name_split)

# #stirng joining by .
# fruits=['apple','banana','grapes']
# fruits_join=" ".join(fruits)
# furits__join=".".join(fruits)
# print(fruits_join)
# print(furits__join)

def nametag(first_name, last_name):
	return("{first_name}{last_name}.".format(first_name=first_name,last_name=last_name[0]))
print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 