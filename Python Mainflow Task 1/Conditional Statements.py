a = 33
b = 200
if b > a:
  print("b is greater than a")
  
print("Completed displaying next conditional output")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
print("Completed displaying next conditional output")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
print("Completed displaying next conditional output")

#Short hand method

if a > b: print("a is greater than b")

#Terenary statements

print("Completed displaying next conditional output")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


print("Completed displaying next conditional output")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
print("Completed displaying next conditional output")

a = 36
b = 2353
if not a > b:
  print("a is NOT greater than b")
  
  
# Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#Pass statement

a = 33
b = 200

if b > a:
  pass