#!/usr/bin/env python3

import sys
from random import randint

def main():
    magic_num = randint(0, 10)
    num_guess = int(input("Please guess an integer between 0 and 10 (inclusive): "))
    if magic_num == num_guess:
        print("You got it!")
    else:
        print("Your guess was not correct.  Please try again!")


if __name__ == "__main__":
    sys.exit(main())
