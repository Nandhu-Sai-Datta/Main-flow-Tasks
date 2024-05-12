# Creating a Tuple with
# the use of Strings
Tuple = ('Food', 'For')
print("\nTuple with the use of String: ")
print(Tuple)
	
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)

# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])

# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(Tuple[-1])

print("\nThird last element of tuple")
print(Tuple[-3])

#Tuple merging

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
mergedTuple = tuple1 + tuple2
print(mergedTuple)

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
mergedTuple = tuple(x for x in tuple1 if x % 2 == 0) + tuple(x for x in tuple2 if x % 3 == 0)
print(mergedTuple)

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
	pri