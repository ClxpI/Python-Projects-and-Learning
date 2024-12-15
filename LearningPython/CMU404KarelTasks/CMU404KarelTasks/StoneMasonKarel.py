
from karel.stanfordkarel import *


def main():
    put()
    while front_is_clear():
        up()
        down()
        move_right()
        put()
        if front_is_blocked():
            up()
            down()
        
def up():
    turn_left()
    while front_is_clear():
        move()
        put()

def down():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def put():
    if beepers_present():
        pick_beeper()
        put_beeper()
    else:
        put_beeper()

def move_right():
    for i in range(4):
        move()


if __name__ == "__main__":
    run_karel_program("SampleQuad2.w")
