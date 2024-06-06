# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['Name']) 

# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get(1)) 

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(f'{key}: {my_dict[key]}')
    
# Modifying an existing key's value
my_dict['a'] = 31

# Adding a new key-value pair
my_dict['d'] = 113

demo_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
item = demo_dict.popitem()
print(item) # ('city', 'New York')
print(demo_dict) # {'name': 'John', 'age': 30}

# code to test slicing
tuple1 = (0 ,1, 2, 3)

print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# Code for deleting a tuple
tuple3 = ( 0, 1)

del tuple3
print(tuple3)

# tuple with different datatypes
tuple_obj = ("immutable",True,23)
print(tuple_obj)

# python code for creating tuples in a loop
tup = ('geek',)

# Number of time loop runs
n = 5
for i in range(int(n)):
	tup = (tup,)
	print(tup)
