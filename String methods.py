
text = 'Nandhu of nOthiG'

# upper() function to convert 
# string to upper case 
print("\nConverted String:") 
print(text.upper()) 

# lower() function to convert 
# string to lower case 
print("\nConverted String:") 
print(text.lower()) 

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:") 
print(text.title()) 

# swaps the case of all characters in the string 
# upper case character to lowercase and viceversa 
print("\nConverted String:") 
print(text.swapcase()) 

# convert the first character of a string to uppercase 
print("\nConverted String:") 
print(text.capitalize()) 

# original string never changes 
print("\nOriginal String") 
print(text)


# using string find() method
print(text.find('of'))


# rjust() 

length = 8

# If no fill character is provided, space 
# is used as fill character 
print(text.rjust(length)) 

my_string = " Hello, world! "
stripped_string = my_string.strip() 

print(stripped_string) 

#Replace method
string = "Good Morning"
new_string = string.replace("Good", "Great")

print("replaced new string is",new_string)

#Index method
print("index of 'nO' in string:", text.index('nO'))
