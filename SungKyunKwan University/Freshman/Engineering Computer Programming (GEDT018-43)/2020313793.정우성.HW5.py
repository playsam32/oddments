#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW5.py
#  Written on : April. 26, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-05, 'Error handling' program
#
#  Modification History:
#     * version 1.0, by 정우성, Apr. 26, 2020
#       - 1st released on this day.
#  end of Modification History
#

"""Module that contains function which can play Guess-A-Number.

In this module there are two functions. get_int() and guess_number()
get_int() gets and returns the integer from user input until input satisfies
the precondition. get_int() is used in guess_number().
If run as script, you can play Guess-A-Number between 1 and 12 with 4 chances.
"""

# Import random module for random number generation.
import random
from eepy import einput as input


def get_int(minimum, maximum):
    """Get an integer given by user.

    User must enter an integer between minimum and maximum. If not,
    this function gives an error message and request number again until
    user gives integer of the range.

    :param minimum: minimum integer which must be given by user.
    :type minimum:  int

    :param maximum: maximum integer which must be given by user.
    :type maximum:  int

    :return: the integer which user enters.
    :rtype:  int

    :precondition: minimum <= maximum
    """
    assert type(minimum) == int, \
        repr(minimum) + ' not valid'
    assert type(maximum) == int, \
        repr(maximum) + ' not valid'
    assert minimum <= maximum, \
        repr(minimum) + ' should be equal or lower than' + repr(maximum)

    valid_input = False
    print(f'I have a number between {minimum} and {maximum}')
    while not valid_input:
        user_input = input(f'Enter the number which I have : ')
        # Check whether user_input is integer or not.
        try:
            # Check wheter it is integer or not.
            user_number = int(user_input)
            # Check if user_input is in valid range.
            # If not, raise ValueError.
            if not (minimum <= user_number <= maximum):
                raise ValueError
        except ValueError:
            error_msg = ('Invalid input: '
                         'Please enter a number between {} and {}'
                         .format(minimum, maximum))
            print(error_msg)
        else:
            # Make line between input line and result line.
            print('')
            valid_input = True

    return user_number


def guess_number(minimum, maximum, max_tries):
    """main program of Guess-A-Number game.

    Simple steps about this game:
        1. Choose answer between minimum and maximum
        2. Check the number of times user tries. If user attempted max_tries
           or more, give the comment and finish the game.
        3. Get user_choice
        4. Check whetehr user_choice is answer or not.
        5. Give useful message about answer.
        6. Repeat step 2 ~ step 5 until user attempts max_tries

    :param minimum: minimum integer which must be given by user.
    :type minimum:  int

    :param maximum: maximum integer which must be given by user.
    :type maximum:  int

    :param max_tries: number of times user can tries.
                      It should be given by users.
                      It also should be valid number. Too many chances or
                      Too few chances should be avoided.
    :type max_tries:  int

    :return: none
    :rtype:  none

    :precondition: minimum <= maximum
                   1 <= max_tries
    """
    assert type(minimum) == int, \
        repr(minimum) + ' not valid'
    assert type(maximum) == int, \
        repr(maximum) + ' not valid'
    assert type(max_tries) == int, \
        repr(max_tries) + ' not valid'
    assert max_tries >= 1, \
        repr(max_tries) + ' should be equal or larger than 1'
    assert minimum <= maximum, \
        repr(minimum) + ' should be equal or lower than' + repr(maximum)

    # Decide a number which user must guess.
    my_number = random.randint(minimum, maximum)
    # Count number of times user tried.
    user_try = 0

    while True:
        user_try += 1

        if user_try > max_tries:
            print(f'My number is {my_number}')
            print(f'You can try {max_tries} times. You lose this game.')
            break

        # Get user input.
        user_choice = get_int(minimum, maximum)

        # Check if user_choice is answer.
        if user_choice == my_number:
            score = max_tries - user_try + 1
            print(f'Your choice is correct, You earned {score} points.')
            break

        # If user tries maximum chance but do not get answer,
        # do not give informations about answers(my_number).
        elif not user_try == max_tries:
            if user_choice < my_number:
                print(f'My number is larger than your choice.')
                minimum = user_choice + 1

            elif user_choice > my_number:
                print(f'My number is less than your choice.')
                maximum = user_choice - 1


# Test if function works well without error.
if __name__ == '__main__':
    guess_number(1, 12, 4)

# -- end of 2020313793.정우성.HW5.py
