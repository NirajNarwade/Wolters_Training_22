# global variable 
# local variable

# enumerate function 
list = ['hi',2,2.5,"anything",False]
for index, item in enumerate(list):
    print(index,item)

# List comprehension
a = [3,2,5,7,23,98,34,567,345,37656,454,56,5345,67,5634,54]
b= [i for i in a if i%2==0]
print(b)

 