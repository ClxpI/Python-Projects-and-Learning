'''
    Author: Mohammad Ismail Ashiq Aslam
    Task: Guessing Game
    
'''

import random
import math

intro = 0
played = 1
guesses = 0
best = 1
def main():
    haiku()
    game()
    rep()

def rep():
    global played
    yes = ["yes","y","yeehaw","YES","Yes","Y"]
    a = input("Do you want to play again? ").strip()
    if a in yes:
        print("")
        played = played + 1
        haiku()
        game()
        a = ""
        rep()
    else:
        x = guesses/played
        print("")
        print("Overall results:")
        print("Total games   =",played)
        print("Total guesses =",guesses)
        print("Guesses/game  =",round(x,1))
        print("Best game     =",best)

def game():
    answer = random.randint(1, 100)
    guess = None
    i = 0
    global best
    b = 0
    global guesses
    while guess != answer:
        guess = input("Your guess? ")
        guess = int(guess)
        guesses = guesses + 1
        i = i + 1
        b = b + 1
        if guess == answer:
            print("You got it right in", i, "guesses!")
            break
        elif guess < answer:
            print("It's higher.")
        else:
            print("It's lower.")
    if b <= best:
        best = played
        

def haiku():
    global intro
    if intro == 0:
        print("A beautiful smile")
        print("That can be seen from a mile")
        print("Makes a better day")
        print("")
        print("I'm thinking of a number between 1 and 100...")
        intro = intro + 1
    else:
        print("I'm thinking of a number between 1 and 100...")
    


main()
