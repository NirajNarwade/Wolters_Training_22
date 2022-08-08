from secrets import choice
import sqlmanager as DbManager
from user import user
import random

# DbManager.create_table()
user_u = None
ch = 1
you = 0
comp = 0
round = 0
choice3 = 1

def user_name():
    global user_u,ch
    ch = 1
    username = input("Enter your name : \n")
    exists = DbManager.get_user_by_name(username)
    # print(exists)
    if exists.__len__() == 0:
        user_u = user(username,0)
        DbManager.insert_user(user_u)
        # print(user_u.name,user_u.score)
        game_start()
    else:
        choice = input("User with this name exists! Do you want to continue with same name?(y/n)\n")
        if(choice=='y'):
            user1 = DbManager.get_user_by_name(username)
            user_u = user(user1[0][0],user1[0][1]) 
            game_start()
            # print(user1[0][0],"**********")
        elif(choice=='n'):
            user_name()
        else:
            print("wrong choice!")
            user_name()

def game_start():
    # print(user_u.name)
    # ch = 1
    # you = 0
    # comp = 0
    # round = 0
    global ch,you,comp,round
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
            user1 = DbManager.get_user_by_name(user_u.name)
            if ch1 == "r":
                if ch2 == "p":
                    you = you + 1
                    print(f"--> Hurrayyy! You won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
                    if(user1[0][1]<you):
                        increment()
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
                    if(user1[0][1]<you):
                        increment()
            elif ch1 == "s":
                if ch2 == "r":
                    you = you + 1
                    print(f"--> Hurrayyy! You won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")
                    if(user1[0][1]<you):
                        increment()
                elif ch2 == "p":
                    comp = comp + 1
                    print(f"--> Damn it! Computer won the game.\n\tRound: {round}\n\tScoreBoard:\n\t\tYou: {you}\n\t\tComputer: {comp}")


    while ch != 3:
        ch = int(input("\t*Press 1 to start.\n\t*Press 2 to reset score.\n\t*Press 3 to go to Main Menu.\n\t"))
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
                ch2 = input(">>> Computer has chosen\n\n>>> Now it's your turn\n\tEnter Your Choice:\n\t\tRock(r)\n\t\tPaper(p)\n\t\tScissors(s)\n\t ")
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
                you = 0
                comp = 0
                round = 0
                print("---   Thank you for playing this game! See you Again.   ---")
                play_game()
            
            case default:
                print("!!!   Enter Correct Choice   !!!")

    # pass

def play_game():
    print("***$$$   Welcome to the Game of Rock Paper and Scissors!   $$$***")
    choice1 = int(input("1. Start\n2. Scoreboard\n3. Exit\n"))
    if choice1 == 1:
        user_name()
    elif choice1 == 2:
        Leaderboard()
    elif choice1 == 3:
        print("See you Soon!!!")
        global choice3
        choice3 = 3
    else:
        print("Enter Correct choice Please!")
        play_game()

def Leaderboard():
    print("***LeaderBoard***")
    userList = DbManager.get_all_users()
    # print(Sort_Tuple(userList))
    sortedList = Sort_Tuple(userList)
    print("name","score")
    for user in sortedList:
        print(user[0],user[1])


def Sort_Tuple(tup):
 
    tup.sort(key = lambda x: x[1])
    tup.reverse()
    return tup
 

def increment():
    DbManager.update_user_score(user_u.name,you)

while choice3 != 3:
    play_game()