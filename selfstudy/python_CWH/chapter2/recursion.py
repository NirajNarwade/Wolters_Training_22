#factorial
def factorial(num):
    if(num==1 or num==0):
        return 1
    return num*factorial(num-1)         # recursion

# print(factorial(5))
# print(factorial(1))
# print(factorial(0))
# print(factorial(3))

#sum of n natural numbers
def sum(num):
    if num==1:
        return 1
    if(num == 0):
        return 0
    return num+sum(num-1)

print(sum(5))

