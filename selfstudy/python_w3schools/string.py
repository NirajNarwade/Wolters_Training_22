# string are arrays
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)
# prints every character one by one

# length of string
a = "Hello, World!"
print(len(a))

# if present
txt = "The best things in life are free!"
print("free" in txt) # True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# if not present
txt = "The best things in life are free!"
print("expensive" not in txt) #True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#   string slicing
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5]) # from start

b = "Hello, World!"
print(b[2:]) # till end

b = "Hello, World!"
print(b[-5:-2]) # negative indexing

# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J")) # "Jello, World"

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

b = a.split(",")
print(type(b))  # returns List

# String Format
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Characters

# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

# String Methods

capitalize()    	#Converts the first character to upper case
casefold()	        #Converts string into lower case
center()	        #Returns a centered string
count()             #Returns the number of times a specified value occurs in a string
encode()	        #Returns an encoded version of the string
endswith()	        #Returns true if the string ends with the specified value
expandtabs()	    #Sets the tab size of the string
find()	            #Searches the string for a specified value and returns the position of where it was found
format()	        #Formats specified values in a string
format_map()	    #Formats specified values in a string
index()	            #Searches the string for a specified value and returns the position of where it was found
isalnum()	        #Returns True if all characters in the string are alphanumeric
isalpha()	        #Returns True if all characters in the string are in the alphabet
isdecimal()	        #Returns True if all characters in the string are decimals
isdigit()	        #Returns True if all characters in the string are digits
isidentifier()	    #Returns True if the string is an identifier
islower()	        #Returns True if all characters in the string are lower case
isnumeric()	        #Returns True if all characters in the string are numeric
isprintable()	    #Returns True if all characters in the string are printable
isspace()	        #Returns True if all characters in the string are whitespaces
istitle() 	        #Returns True if the string follows the rules of a title
isupper()	        #Returns True if all characters in the string are upper case
join()	            #Joins the elements of an iterable to the end of the string
ljust()	            #Returns a left justified version of the string
lower()	            #Converts a string into lower case
lstrip()	        #Returns a left trim version of the string
maketrans()	        #Returns a translation table to be used in translations
partition()	        #Returns a tuple where the string is parted into three parts
replace()	        #Returns a string where a specified value is replaced with a specified value
rfind()	            #Searches the string for a specified value and returns the last position of where it was found
rindex()	        #Searches the string for a specified value and returns the last position of where it was found
rjust()	            #Returns a right justified version of the string
rpartition()	    #Returns a tuple where the string is parted into three parts
rsplit()	        #Splits the string at the specified separator, and returns a list
rstrip()	        #Returns a right trim version of the string
split()	            #Splits the string at the specified separator, and returns a list
splitlines()	    #Splits the string at line breaks and returns a list
startswith()	    #Returns true if the string starts with the specified value
strip()	            #Returns a trimmed version of the string
swapcase()	        #Swaps cases, lower case becomes upper case and vice versa
title()	            #Converts the first character of each word to upper case
translate()	        #Returns a translated string
upper()	            #Converts a string into upper case
zfill()	            #Fills the string with a specified number of 0 values at the beginning