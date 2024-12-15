
from karel.stanfordkarel import *

beeper = True

def main():
    next = True
    while next:
        checker_row()
        next = move_to_next()

def checker_row():
    global beeper
    if beeper:
        put_beeper()
    beeper = not beeper
    while front_is_clear():
        move()
        if beeper:
            put_beeper()
        beeper = not beeper
    return beeper

def move_to_next():
    left = facing_east()
    if left:
        turn_left()
    else:
        turn_right()
    if front_is_clear():
        move()
    else:
        return False
    if left:
        turn_left()
    else:
        turn_right()
    return True

def turn_right():
    turn_left()
    turn_left()
    turn_left()



if __name__ == "__main__":
    run_karel_program("CheckerboardKarel.w ")
    run_karel_program("8x1.w ")
    run_karel_program("1x8.w ")
    run_karel_program("7x7.w ")
    run_karel_program("6x5.w ")
    run_karel_program("3x5.w ")
    run_karel_program("5x3.w ")
    run_karel_program("40x40.w ")
    run_karel_program("1x1.w ")

