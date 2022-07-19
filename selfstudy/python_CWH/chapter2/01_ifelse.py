flag = True
flag1 = False
if flag: 
    print("flag is true")                   # tab after if runs if condition satisfies
    print("flag is true")                   # tab after if runs if condition satisfies
print("falg is false")                      # whatever is not tab then it is not considered as part of if statement

if flag1: 
    print("flag is true")                   # tab after if runs if condition satisfies
    print("flag is true")                   # tab after if runs if condition satisfies
else:
    print("falg is false")                  # else executed if condition does not satisfies

# if else ladder
# if condition:
#   do something
# elif condition:
#   do something
# elif condition:
#   do something
# elif condition:
#   do something
# else:
#   do something 

# relational operators
# == --> comparison
# <  -->less than
# >  -->greater than
# <= -->less than equal to
# >= -->greater than equal to
# != -->not equal to
# logical operators 
# and --> both true
# or --> any one true
# not --> changes to opposite
#  

# Examples
# program to find greatest of four numbers take input from user

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

if num1>num4:
    f1 = num1
else:
    f1 = num4
if num2>num3:
    f2 = num2
else:
    f2 = num3

if f1 > f2:
    print(f1, "is greater amongst ",num1,num2,num3,num4)
else:
    print(f2, "is greater amongst ",num1,num2,num3,num4)

# this code is complete and works


# program to find wheter student is pass or fail
# condition 3 subs,40% in total, 33% in each sub/ take input from user 

sub1 = float(input("Enter marks of subject 1 : "))
sub2 = float(input("Enter marks of subject 2 : "))
sub3 = float(input("Enter marks of subject 3 : "))
total = (sub1+sub2+sub3)/300*100
if sub1>=33 and sub2>=33 and sub3>=33 and total>=40:
    print("pass")
else:
    print("fail")

if(sub1<33 or sub2<33 or sub3<33):
    print("Failed: Reason - due to less marks in subject (min 33% required)")
elif total<40:
    print("Failed: Reason - due to less Overall marks (min 40% required)")
else:
    print("Congratulations! you have successfully passed examination and scored",total,"percantage")

# this code is complete and works


# program to detect spam
# if contains "make alot of money","buy now","subscribe this","click this"

str = "My name is Niraj Narwade"
str1 = "make a lot of money"
str2 = "buy now"
str3 = "subscribe this"
str4 = "click this"

text = input("Enter text : ")

if "make a lot of money" in text or "buy now" in text or "subscribe this" in text or "click this" in text:
    print("spam")
else:
    print("Not a spam")