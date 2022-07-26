# functions

# def hello():
#     str = input("Enter your name:\n")
#     print(f"Hello {str}, Good Morning!\nHave a great day...")


def bark():
    print("woof Woof WOOF!!!")
    print("dog is barking...")


bark()
# hello()


# parameterized function

def hi(name):
    print(f"Hii {name}")


hi("Niraj")


def addition(a, b, c):
    print(f"Addition of {a}, {b}, {c} is {a+b+c}")


addition(2, 5, 9)


def misc(p, q, r, s, t):
    print(f"{p} is {q} and has wokerd on {r} projects in last {s} years and experience of total {t} years")


misc("Niraj", "Software Engineer", 12, 2, 6)


# returning Function
def double(num):
    return num * 2


number = double(4)
print(number)

# function returning string in all caps


def caps(text):
    return text.upper()


print(caps("my name is niraj"))

# all above are positional arguments
# while calling function they are passed sequencially


def fnc(name, age):
    print(f"{name} is {age} years old")


fnc('Niraj', 27)
fnc(27, 'niraj')
fnc(name='niraj', age=27)            # order does not matter now
fnc(age=27, name='niraj')

#  default parameters
#  variable parameter function

# functions cwh
marks1 = [83, 65, 78, 43]

marks2 = [93, 75, 68, 73, 65]

def fnc1(list):
    return (sum(list)/len(list))

print(fnc1(marks1), fnc1(marks2))

def greet(name = "Niraj"):          #default parameter
    print("Hello "+name+", How are you?")

greet("Simba")      #parameter passed
greet()             #parameter not passed

# * pattern
for i in range(5):
    print("*" * (5-i))


