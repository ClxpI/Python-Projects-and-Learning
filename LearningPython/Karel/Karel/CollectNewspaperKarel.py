
from karel.stanfordkarel import *


def main():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program("CollectNewspaperKarel.w")
