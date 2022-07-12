

amt = int(input(("Enter amount to calculate discount : \n")))

if amt<=1000:
    amt=amt-(amt*5/100)
    print("Applicable discount is: 5%\nDiscounted amount is ", amt)
elif amt>1000 and amt<=5000:
    amt=amt-(amt*10/100)
    print("Applicable discount is: 10%\nDiscounted amount is ", amt)
else :
    amt=amt-(amt*15/100)
    print("Applicable discount is: 15%\nDiscounted amount is ", amt)


print("Additional Discount :")

age = int(input("Enter your Age : \n"))
privileged = input("Are you privileged user(yes/no) : \n")
if privileged.lower()=="yes":
    flag = True
elif privileged.lower()=="no":
    flag = False
else:
    print("invalid input!!!")
    flag = False


if(age>70):
    amt=amt-(amt*5/100)
    print("for members over 70 years additional discount is 5%\nNow discounted amount is ",amt)
if(flag):
    amt=amt-(amt*5/100)
    print("for Priveleged members addictional discount is 5%\nNow discounted amount is ",amt)
