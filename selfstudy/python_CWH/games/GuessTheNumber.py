import random
import time

print("Hello there..! Welcome to GuessTheNumber game!\nI'm going to pic a number from 1 - 100.")

print("\nPicking a number now!")
time.sleep(2)
num = int(input("\nwhat is your guess?: "))
correct_num = random.randint(1,100)
trials = 1

while num!=correct_num:
    #print(correct_num)
    if(num<correct_num):
        print("\nGuess Higher!\nCorrect number is bigger")
    if(num>correct_num):
        print("\nGuess Lower!\nCorrect number is smaller")
    num = int(input("\nwhat is your guess this time?: "))
    trials +=1

print(f"\n\nYou made it!!!\n\nIt's a correct Number\n\nYou took {trials} attempts this time\n")