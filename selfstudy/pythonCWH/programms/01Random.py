import random

print(random.randint(1,10))

print(random.random())


# yes/no/maybe program

num = random.randint(1,3)
if num==1:
    print("Yes")
if num==2:
    print("No")
if num==3:
    print("Maybe")


# Lucky Number number
lucky_num = random.randint(1,100)
if lucky_num<=20:
    print(f"you'll Have a good day! your lucky number today is {lucky_num}")
if lucky_num<=40 and lucky_num>20:
    print(f"you'll Have a great day! your lucky number today is {lucky_num}")
if lucky_num<=60 and lucky_num>40:
    print(f"you'll Have a fantastic day! your lucky number today is {lucky_num}")
if lucky_num<=80 and lucky_num>60:
    print(f"you'll Have a excellent day! your lucky number today is {lucky_num}")
if lucky_num<=100 and lucky_num>80:
    print(f"you'll Have a wonderful day! your lucky number today is {lucky_num}")       


# another lucky number program
my_num = random.randint(1,100)
n = random.randint(1,3)
text = ''
if n==1:
    text = "You'll have a great day!"
if n==2:
    text = "Take care today!"
if n==3:
    text = "Today is your Lucky Day!!!"

print(f"{text} your lucky number is : {my_num}")
