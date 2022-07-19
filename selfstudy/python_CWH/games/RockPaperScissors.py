import random
print("Welcome to Rock Paper and Scissors!")
ch = 1
you = 0
comp = 0
def game(ch1,ch2):
    global you,comp
    if ch1 == "r":
        if ch2 == "r":
            print(f"Oops! It's a tie...Try again.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
        elif ch2 == "p":
            you = you + 1
            print(f"Hurrayyy! You won the game.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
        elif ch2 == "s":
            comp = comp + 1
            print(f"Damn it! Computer won the game.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
    elif ch1 == "p":
        if ch2 == "r":
            comp = comp + 1
            print(f"Damn it! Computer won the game.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
        elif ch2 == "p":
            print(f"Oops! It's a tie...Try again.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
        elif ch2 == "s":
            you = you + 1
            print(f"Hurrayyy! You won the game.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
    elif ch1 == "s":
        if ch2 == "r":
            you = you + 1
            print(f"Hurrayyy! You won the game.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
        elif ch2 == "p":
            comp = comp + 1
            print(f"Damn it! Computer won the game.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")
        elif ch2 == "s":     
            print(f"Oops! It's a tie...Try again.\n\tScore:\n\tYou: {you}\n\tComputer: {comp}")


while ch != 3:
    ch = int(input("Press 1 to start.\n\tPress 2 to reset score.\n\tPress 3 to exit.\n\t"))
    match ch:
        case 1:
            n = random.randint(1,3)
            if(n==1):
                ch1 = "r"
            elif(n==2):
                ch1 = "p"
            elif(n==3):
                ch1 = "s"
            ch2 = input("Computer has choosen\n\tNow it's your turn\n\t\tEnter Your Choice:\n\t\tRock(r)\n\t\tPaper(p)\n\t\tScissors(s)\n\t ")
            print(ch2)
            if ch2 != "r" and ch2 != "p" and ch2 != "s":
                print("Enter Correct Choice!")
            else:
                game(ch1,ch2)

        case 2:
            you = 0
            comp = 0
            print("Scores have been reset. Now you can Fresh start!")
        case 3:
            print("Thank you for playing this game!")
        
        case default:
            print("Enter Correct Choice!")


# player1 = input("Player 1 Enter Your Choice:\n\tRock(r)\n\tPaper(p)\n\tScissors(s)").lower
# player2 = input("player 2 Enter Your Choice:\n\tRock(r)\n\tPaper(p)\n\tScissors(s)").lower

# if player1 == 'r' and player2 == 'p':
#     print("Player 2 Won this game")
