# #while loop

# x = 0
# while x < 5:
#   print("Not there yet, x=" + str(x))
#   x = x + 1
# print("x=" + str(x))

# def attempt(n):
#     x=0
#     while n>x:
#         print("The attempt is:"+str(x))

#         x+=1
# attempt(7)
# print("Done")

def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)


def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n=n+1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT