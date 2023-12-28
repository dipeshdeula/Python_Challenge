def format_name(first_name, last_name):
	if len(first_name)!=0 and len(last_name)!=0:
		return "Name:"+str(last_name),str(first_name)
	elif len(first_name)==0 and len(last_name)>0:
		return "Name:"+str(last_name)
	elif len(first_name)>0 and len(last_name)==0:
		return "Name:"+str(first_name)
	else:
		return "Empty String"
	

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2)>=len(word1) and len(word2)>=len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# The fractional_part function divides the numerator by the denominator, and returns just 
# the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	#frac=numerator%denominator
	if(denominator)==0:
		return 0
	else:
		a= numerator/denominator
		b=int(numerator/denominator)
		c=a-b
		return c
	
# keep just the fractional part of the quotient
	

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0