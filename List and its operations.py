# Creating a List with 
# the use of multiple values 
List = ["Orage", "Hii", "Good"] 
print("\nList containing multiple values: ") 
print(List)

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List2 = [['Apple', 'For'], ['Food']] 
print("\nMulti-Dimensional List: ") 
print(List2) 

# accessing a element from the 
# list using index number 
print("Accessing element from the list") 
print(List[0]) 
print(List[2]) 

# accessing a element using 
# negative indexing 
print("Accessing element using negative indexing") 
	
# print the last element of list 
print(List[-1]) 
	
# print the third last element of list 
print(List[-3])

# create a list of numbers
my_list = [1, 2, 3, 4, 5]
print(my_list)
# [1, 2, 3, 4, 5]

# replace the second element with 10 using indexing
my_list[1] = 10
print(my_list)
# [1, 10, 3, 4, 5]

# replace the last two elements with 6 and 7 using slicing
my_list[-2:] = [6, 7]
print(my_list)
# [1, 10, 3, 6, 7]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

combined_list = list1 + list2
print(combined_list)


my_list = ['sling', 'academy', 'dog', 'turtle', 'dog', 'turkey', 'dog']
my_list.remove('dog')
print(my_list)

# a list of video games
games = [
    "Minecraft",
    "Fortnite",
    "CS:GO"
]

# Insert a game at index 2
games.insert(2, "League of Legends")
print(games)