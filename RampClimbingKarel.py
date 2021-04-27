from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    # karel puts beeper at initial position
    put_beeper()
    # karel putting beeper on two row forward and
    # a column upward from the last beeper
    while front_is_clear():
        move_to_next_row()
        put_beeper()


# making karel move two row forward
# and a column upward
def move_to_next_row():
    for i in range(2):
        move()
    turn_left()
    move()
    turn_right()


# making karel turn right
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('RampKarel1.w')
