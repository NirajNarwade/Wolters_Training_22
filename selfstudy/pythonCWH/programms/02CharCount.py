str = "a b c d E s d i s d i k j d a l k d n E a m n f m e f l k a m D a j d o i a j f i a j n f m a s c a m s n D w l i"

# print(str.split())
char_count={}
for char in str.lower().split():        # convert in lower case then split
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

