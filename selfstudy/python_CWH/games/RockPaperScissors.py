import random
print("Welcome to Rock Paper and Scissors!")
ch = 1
you = 0
comp = 0
def game(ch1,ch2):
    if ch1 == "r":
        if ch2 == "r":
            print("Oops! It's a tie...Try again.\nScore:\nYou: "+you+"\nComputer: "+comp)
        elif ch2 == "p":
            you = you + 1
            print("Hurrayyy! You won the game.\nScore:\nYou: "+you+"\nComputer: "+comp)
        elif ch2 == "s":
            comp = comp + 1
            print("Damn it! Computer won the game.\nScore:\nYou: "+you+"\nComputer: "+comp)
    elif ch1 == "p":
        if ch2 == "r":
            comp = comp + 1
            print("Damn it! Computer won the game.\nScore:\nYou: "+you+"\nComputer: "+comp)
        elif ch2 == "p":
            print("Oops! It's a tie...Try again.\nScore:\nYou: "+you+"\nComputer: "+comp)
        elif ch2 == "s":
            you = you + 1
            print("Hurrayyy! You won the game.\nScore:\nYou: "+you+"\nComputer: "+comp)
    elif ch1 == "s":
        if ch2 == "r":
            you = you + 1
            print("Hurrayyy! You won the game.\nScore:\nYou: "+you+"\nComputer: "+comp)
        elif ch2 == "p":
            comp = comp + 1
            print("Damn it! Computer won the game.\nScore:\nYou: "+you+"\nComputer: "+comp)
        elif ch2 == "s":     
            print("Oops! It's a tie...Try again.\nScore:\nYou: "+you+"\nComputer: "+comp)


while ch != 2:
    ch = int(input("Press 1 to start.\nPress 2 to exit.\n"))
    match ch:
        case 1:
            n = random.randint(1,3)
            if(n==1):
                ch1 = "r"
            elif(n==2):
                ch1 = "p"
            elif(n==3):
                ch1 = "s"
            ch2 = input("Computer has choosen\nNow it's your turn\n\tEnter Your Choice:\n\tRock(r)\n\tPaper(p)\n\tScissors(s)\n ")
            print(ch2)
            if ch2 != "r" and ch2 != "p" and ch2 != "s":
                print("Enter Correct Choice!")
            else:
                game(ch1,ch2)

        case 2:
            print("Thank you for playing this game!")
        
        case default:
            print("Enter Correct Choice!")


# player1 = input("Player 1 Enter Your Choice:\nRock(r)\nPaper(p)\nScissors(s)").lower
# player2 = input("player 2 Enter Your Choice:\nRock(r)\nPaper(p)\nScissors(s)").lower

# if player1 == 'r' and player2 == 'p':
#     print("Player 2 Won this game")
