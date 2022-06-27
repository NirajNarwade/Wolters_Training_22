a = 'Niraj'
b = "Niraj"
c = '''Niraj'''



fname = "Niraj"
lname = "Narwade"
print(fname+" "+lname)
print(fname[1])                 #char at [number] in string / only reading --> (i)
#print(fname[6])                 #error --> not possible for string with length 5
#  string slicing
print(fname[0:3])               # char at 0 1 2 (substring) --> start 0, end 3 --> (Nir)
print(fname[-1])                # negative indexes reads from last char --> (j)
                                #  0  1  2  3  4  5
                                # -6 -5 -4 -3 -2 -1

#  string slicing with skip value
d = fname[0:4:2]                # try diff variations
print(d)

# string functions
print(len(fname))               # length()
print(fname.endswith("j"))      # boolean
print(fname.count("ir"))        # counts char or string
print(fname.capitalize())       # capitalize first letter
print(fname.find("j"))          # finds if exists returns first occurance index else -1

# escape sequence  characters
# \n new line
# \t tab spaces
# \\ to print one \

# misc fnc
letter = '''hi <|name|>
Good Morning
today is <|date|>'''
name = input("Enter your name:\n")
date = input("Enter Date:\n")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)

# String with variables
day = 21
month = "Aug"
temp = 27.4

print(f"Today is {month} {day} and it's {temp} degrees outside")


str = '''abcd
efgh
ijkl
mnop
qrst
uvwx
yz'''
print (str)
print(str.split())
print(len(str))
print(len(str.split()))


for word in str.split():
    print(word)