# print syntax
print("Hello, World!")  # Hello, World! 

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x+y)

x = 5
y = "niraj"
print(x, y)

# if statement / indentation
if 5 > 2:
  print("Five is greater than two!")

# variables
x = 5
y = "Hello, World!"

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

# type of variable
x = 5
y = "Niraj"
print(type(x))
print(type(y)) 

x = "Niraj"
# is the same as
x = 'Niraj'

a = 4
A = "Sally"
#A will not overwrite a 

# legal variable names
myvar = "Niraj"                                 
my_var = "Niraj"
_my_var = "Niraj"
myVar = "Niraj"
MYVAR = "Niraj"
myvar2 = "Niraj"

# illegal variable names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi Words Variable Names

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# global variables --> not part of any function / decleared outside function
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# global keyword --> 
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 

