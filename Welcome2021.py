from karel.stanfordkarel import *

"""
File: Welcome2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""


def main():
    # making karel put 20 beepers
    for i in range(20):
        put_beeper()
    move()
    # making karel put 21 beepers
    for i in range(21):
        put_beeper()
    move()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('3x3.w')
