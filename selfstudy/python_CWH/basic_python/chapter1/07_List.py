a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    0 1 2 3 4 5 6 7 8   indexes
#   -9-8-7-6-5-4-3-2-1   indexes
print(a)

# accessing elements using indexes
print(a[0])

# modification possible using indexes
a[0] = 12
print(a)

# List of many types
b = [45, 'niraj', False, 45.54]
print(b)

#  list slicing 0 1 2
print(a[0:3])
#  list slicing -5 -4 -3
print(a[-5:-2])

# sorting
list = [34, 546, 7, 2, 86, 98, 45, 23, 2]
print(list)
list.sort()
print(list)

# reverse
list.reverse()
print(list)

# append
list.append(1233)
print(list)

# insert
list.insert(3, 33)  # inesert 33 at 3rd index
print(list)

# deleting element from list
list.remove(2)  # removes element with value (first occurance)
print(list)
list.pop(3)    # removes element at 3rd index
print(list)
del(list[2])   # deletes item from index 2
print(list)
# sum of all elements
print(sum(list))
