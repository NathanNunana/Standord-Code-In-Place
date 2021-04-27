from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    # function calls
    pick_last_puzzle()
    put_puzzle_in_place()
    move_to_initial_position()


# making karel move to and pick up the last piece
def pick_last_puzzle():
    for i in range(2):
        move()
    pick_beeper()


# making karel fix the last piece of the puzzle
def put_puzzle_in_place():
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()


# making karel move back to the initial position
def move_to_initial_position():
    turn_around()
    for i in range(2):
        move()
    turn_right()
    for i in range(3):
        move()
    turn_around()


# making karel turn right
def turn_right():
    for i in range(3):
        turn_left()


# making karel turn around
def turn_around():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Puzzle.w')
