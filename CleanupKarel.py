from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""

def main():
    """
    making karel move if its not facing a wall and making it pick
    beepers if there is some present at it's location
    """
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()


if __name__ == '__main__':
    run_karel_program('Cleanup2.w')