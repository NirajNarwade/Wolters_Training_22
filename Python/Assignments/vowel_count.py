inputstr = input('Enter a string:')
inputstr = inputstr.casefold()
print(inputstr)
vowels = 'aeiou'

# vlist = []
# for char in inputstr:
#     if char in vowels:
#         vlist.append(char)
#
# print(vlist)
#
# count total number of vowels
# num_vowels = [vowel for vowel in inputstr if vowel in vowels]
# print((len(num_vowels), num_vowels))

# count number of times each vowel occurs
# vowel_count = {}.fromkeys(vowels, 0)
# print(vowel_count)
# for char in inputstr:
#     if char in vowels:
#         vowel_count[char] += 1
#
# print(vowel_count)

def num_vowels(input):
    num_vowels = [vowel for vowel in input if vowel in vowels]
    return num_vowels

print(num_vowels(inputstr))