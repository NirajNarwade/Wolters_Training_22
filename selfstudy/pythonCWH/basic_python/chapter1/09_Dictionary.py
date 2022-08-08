# dictionary --> key value pairs
# duplicate keys not allowed

# declaration
emptyDictionary = {}
myDictionary = {
    "one":"1",
    "two":2,
    3:"3",
    "four":4,
    "marks": [1,4,8],                                                   # list in dictionary
    "anotherDictionary" : { "hi":"Niraj","greetings":"good morning"}    # another dictionary in dictionary
}

print(myDictionary)                                                     # prints all dictionary
print(myDictionary["four"])                                             # print value associated with key
print(myDictionary["marks"])                                            # print list
print(myDictionary["marks"][0])                                         # print list item at particular index
print(myDictionary["anotherDictionary"])                                # print another dictionary
print(myDictionary["anotherDictionary"]["hi"])                          # print value associated with key in dictionary in another dictionary

print(myDictionary.keys())                                              # prints all keys
print(myDictionary.values())                                            # prints all values
print(myDictionary.items())                                             # prints keys with values

updateDictionary = {
    "new_key" : "new value"
}

myDictionary.update(updateDictionary)                                   # appends if not present or updates if key is present
print(myDictionary)

print(myDictionary.get("one"))                                          # returns value if key if present
print(myDictionary.get("five"))                                         # returns null if key is not present
#print(myDictionary["five"])                                            # throws error if key is not present

myDictionary["another_new"] = "another new value"                       # appends new pair at the end of dictionary
print(myDictionary)

del(myDictionary["another_new"])                                        # deletes particular pair
print(myDictionary)

del(myDictionary)                                                       # deletes variables also
print(myDictionary)
