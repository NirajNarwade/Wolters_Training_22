
input_str = input('Enter a string: ')
input_str = input_str.casefold()

words_in_str = input_str.split()
print(words_in_str)

even_words = []
for word in words_in_str:
    if len(word) % 2 == 0:
        even_words.append(word)

print(even_words)