# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 4, 'For', 6, 'POwer'])
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
	print(i, end =" ")
print()

# Checking the element
# using in keyword
print("POwer" in Set)

# Program to perform different set operations
# as we do in mathematics

# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)

#Python Set Methods

fruits = {"apple", "banana", "cherry"}
fruits.add("mango")  # Adding a new element
print(fruits)  # Output: {'apple', 'cherry', 'mango', 'banana'}
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set() (empty set)

fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")  # No error even if element doesn't exist
print(fruits)  # Output: {'apple', 'cherry', 'banana'}


fruits = {"apple", "banana", "cherry"}
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: One of the fruits (order may vary)
print(fruits)        # Remaining fruits (order may vary)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# This will raise a KeyError because "orange" isn't present
# fruits.remove("orange")
