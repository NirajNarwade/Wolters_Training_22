#try except
ch = ''
while(ch != 'q'):
    print("press q to quit")
    a = input("Enter a number:\n")
    if(a == 'q'):
        break
    
    try:
        a = int(a)
    except Exception as e:
        print(e)
    
    print(f"You have entered: {a}")


#try except else

try:
    print("hi")
except Exception as e:
    print(e)
else:                   #gets executed only when try is successful
    print("something")

#try with finally

try:
    print("hii")
except Exception as e:
    print(e)
finally:                #always gets executed
    print("bye")