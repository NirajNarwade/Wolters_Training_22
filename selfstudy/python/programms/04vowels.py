# my solution
str = input("Enter a string: ")
a_cnt = 0
e_cnt = 0
i_cnt = 0
o_cnt = 0
u_cnt = 0
v_cnt = 0 
# str.casefold() --> more efficient search more on this
for char in str.lower():
    if(char=='a'):
        a_cnt+=1
        v_cnt+=1
    if(char=='e'):
        e_cnt+=1
        v_cnt+=1
    if(char=='i'):
        i_cnt+=1
        v_cnt+=1
    if(char=='o'):
        o_cnt+=1
        v_cnt+=1
    if(char=='u'):
        u_cnt+=1
        v_cnt+=1

print("Total number of vowels in given string is",v_cnt)
print(" a -->",a_cnt)
print(" e -->",e_cnt)
print(" i -->",i_cnt)
print(" o -->",o_cnt)
print(" u -->",u_cnt)
    


# Another solution(from Nagraj sir)

inputstr = input("Enter some string: ")
inputstr = inputstr.casefold()
vowels = 'aeiou'

num_vowels = [vowel for vowel in inputstr if vowel in vowels]
print((len(num_vowels), num_vowels))
# vowel_count = {
#     'a': 0,
#     'e': 0,
#     'i': 0,
#     'o': 0,
#     'u': 0
# }

vowel_count = {}.fromkeys(vowels,0)     # altrnate syntax for line 45-50

for char1 in inputstr:
    if char1 in vowels:
        vowel_count[char1]+=1
print(vowel_count)


# using function
def num_vowel(str1):
    vowel1 = 'aeiou'
    num_vowel1 = [vowel for vowel in str1 if vowel in vowel1]
    return len(num_vowel1)

print(num_vowel("my name is niraj"))