import random
import time
print("***$$$   Welcome to the Game of Rock Paper and Scissors!   $$$***")
ch = 1
you = 0
comp = 0
round = 0
def game(ch1,ch2):
    global round
    round+=1
    if ch1 == "r":
        ch3 = "Rock"
    elif ch1 == "p":
        ch3 = "Paper"
    else:
        ch3 = "Scissors"
    if ch2 == "r":
        ch4 = "Rock"
    elif ch2 == "p":
        ch4 = "Paper"
    else:
        ch4 = "Scissors"
    global you,comp
    print(f"Computer chose {ch3}\nYou chose {ch4}")
    if ch1 == ch2 :
        print(f"--> Oops! It's a tie...Try again\n\tRound: {round}.\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
    else:
        if ch1 == "r":
            if ch2 == "p":
                you = you + 1
                print(f"--> Hurrayyy! You won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
            elif ch2 == "s":
                comp = comp + 1
                print(f"--> Damn it! Computer won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
        elif ch1 == "p":
            if ch2 == "r":
                comp = comp + 1
                print(f"--> Damn it! Computer won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
            elif ch2 == "s":
                you = you + 1
                print(f"--> Hurrayyy! You won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
        elif ch1 == "s":
            if ch2 == "r":
                you = you + 1
                print(f"--> Hurrayyy! You won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
            elif ch2 == "p":
                comp = comp + 1
                print(f"--> Damn it! Computer won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")


while ch != 3:
    ch = int(input("\t*Press 1 to start.\n\t*Press 2 to reset score.\n\t*Press 3 to exit.\n\t"))
    match ch:
        case 1:
            print(">>> Computer's turn\n\tComputer is making a choice:\n\t\tRock(r)\n\t\tPaper(p)\n\t\tScissors(s)\n\t ")
            n = random.randint(1,3)
            if(n==1):
                ch1 = "r"
            elif(n==2):
                ch1 = "p"
            elif(n==3):
                ch1 = "s"
            # time.sleep(2)
            ch2 = input(">>> Computer has choosen\n\n>>> Now it's your turn\n\tEnter Your Choice:\n\t\tRock(r)\n\t\tPaper(p)\n\t\tScissors(s)\n\t ")
            print(ch2)
            if ch2 != "r" and ch2 != "p" and ch2 != "s":
                print("!!!   Enter Correct Choice   !!!")
            else:
                game(ch1,ch2)

        case 2:
            you = 0
            comp = 0
            round = 0
            print("<<<   Scores have been reset. Now you can Fresh start!   >>>")
        case 3:
            print("---   Thank you for playing this game! See you Again.   ---")
        
        case default:
            print("!!!   Enter Correct Choice   !!!")

