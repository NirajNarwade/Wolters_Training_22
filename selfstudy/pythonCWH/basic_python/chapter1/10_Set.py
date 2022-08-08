# collection of non repetetive elements
# unordered - unindexed 

emptySet = set()                # creates empty set
set = {1,2,3.1,4,1,"1"}         # skips repeated value but kept string as it is not int 
print(set)

set.add(5)                      # appends 5
set.add(5)                      # does nothing
print(set)
print(len(set))                 # length of set

set.remove(1)                   # removes value from set
# set.remove(14)                # error if value is not present in set
print(set)

print(set.pop())                # removes element
print(set)

set.clear()                     # removes all elements
print(set)
print(len(set))
set.add(20)
print(len(set))