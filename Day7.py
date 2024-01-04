# #leap year
# def year(n):
#     if (n % 4 == 0):
#         print("Year is leap")
#     else:
#         print("Year is not leap")
    
# calendar=year(4)
# print(calendar)

# #user input
# year=input('year you want to check:')
# year_num=int(year)
# if year_num %4 == 0:
#     print(year_num,'is a leap year')
# else:
#     print(year_num,"is not a leap year")

#word count
# text='Love to do Coding'
# count=0
# for i in text.split():
#     count+=1
#     print('Total words',count)

# sentence=input('Enter a sentence')
# count=0
# for char in sentence:
#     if char==' ':
#         count=count+1
# count+=1
    
# print('Total sentences:',count)

#count vowels
# text=input("Enter a sentence:\t")
# count=0
# for letter in text.lower():
#     if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
#         count +=1

# print("vowel letter:",str(count))

def count_vowels(sentence):
    count=0
    vowels=['a','A','e','E','i','I','o','O','u','U']
    for char in sentence:
        if char in vowels:
            count +=1
    print("Total no. of Vowel letter is :",str(count)) 
count_vowels("HELLO World, My name is Dipesh")

