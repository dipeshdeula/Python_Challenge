#some basic list keyword of python

list_Pro=['c','java','python']
print(list_Pro)

#list is like a array in python but yesma sabai data type fit hunxa
list_index=list_Pro.index('java')
print(list_index)

#list lai thapnu paryo vani append user garni
planets=["abc"]
planets.append("def")
print(planets)


#get value by index
print(list_Pro[2])

#len keyword helps to count total no. of element in the lis

list_count=len(list_Pro)
print(list_count)

#remove keyword helps to remove element form the list
list_remove=list_Pro.remove("java")
print(list_remove)

#set by index
friends=['ram','sita','hari']
friends[0]='ramesh'
print(friends)

#min and max elements from the list
num=['2','0','-1','5']
print(min(num))
print(max(num))

#element exist use in keyword if element exist return true else false
#example friends list
print("sita" in friends)
print("shreya" in friends)

#concat lists
first_nums=[1,2,3,4,5]
second_nums=[6,7,8,9,10]
all_nums = first_nums + second_nums
print(all_nums)

#pop keyword use to kick out the last element from the list
# for example we have to kick 10 from the all_nums then
all_nums.pop()
print(all_nums)

#list sorts
fruits=["banana","apple","cherry"]
fruits.sort() #this will sort the fruits list alphabetically
print(fruits)

#list range
numbers=list(range(1,11))
print(numbers)

#sum of list
total=sum(numbers)
print(total)

#find keyword is used to find a specific item in the list
index=numbers.index(5)
print(index)

#insert list element-> inserts the element at the given index, shifting elements to the right
numbers.insert(3,99)
print(numbers)

#list exend -> adds the elements in list to the end of the list
more_numbers=[11,12,13,14]
numbers.extend(more_numbers)
print(numbers)