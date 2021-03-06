from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    repair_arches()
    while front_is_clear():
        next_arche()
        repair_arches()


def repair_arches():
    fix_column()
    descend_arche()


def fix_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()


def descend_arche():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def next_arche():
    for i in range(4):
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('SampleQuad1.w')
