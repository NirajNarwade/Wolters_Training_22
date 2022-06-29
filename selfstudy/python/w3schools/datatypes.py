# Built-in Data Types

# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType 

x = "Hello World" 	                            #str 	        x = str("Hello World")
x = 20 	                                        #int 	        x = int(20)
x = 20.5 	                                    #float 	        x = float(20.5)
x = 1j 	                                        #complex 	    x = complex(1j)
x = ["apple", "banana", "cherry"] 	            #list 	        x = list(("apple", "banana", "cherry"))
x = ("apple", "banana", "cherry") 	            #tuple 	        x = tuple(("apple", "banana", "cherry"))
x = range(6) 	                                #range 	        x = range(6)
x = {"name" : "John", "age" : 36} 	            #dict 	        x = dict(name="John", age=36)
x = {"apple", "banana", "cherry"} 	            #set 	        x = set(("apple", "banana", "cherry")) 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	    x = frozenset(("apple", "banana", "cherry")) 	
x = True 	                                    #bool 	        x = bool(5)  	
x = b"Hello" 	                                #bytes 	        x = bytes(5) 	
x = bytearray(5) 	                            #bytearray 	    x = bytearray(5)	
x = memoryview(bytes(5)) 	                    #memoryview 	x = memoryview(bytes(5))
x = None 	                                    #NoneType   

# Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# for random number
import random
print(random.randrange(1, 10))



