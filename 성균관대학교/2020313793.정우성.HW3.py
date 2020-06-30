#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW3.py
#  Written on : April. 12, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-03, 'If/while statement' program
#
#  Modification History:
#     * version 1.0, by 정우성, Apr. 12, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""This is the module that contains print_randoms() function which print random
integers and print average under the whole integer's line.

There are three functions in this module:
    helper_maxdigit()
    helper_nspaces()
    print_randoms()
Two helper functions are used to help print_randoms().
Three constants, WIDTH, MINSPACES and MAXSPACES, are used in helper functions.
Brief steps,
First, helper_maxdigit() finds max digits of integers in range using arguments
of print_randoms() ,and assign them as local variable in print_randoms().
Second, helper_nspaces() finds  the compilation of whitespaces using max digits
and arguments of print_randoms(). Then also assign the as local variable too.
Finally, use those local variables to print integers.
"""

# Import random module for random number generation.
import random

# Default constants
# WIDTH     : width of Mac Terminal or Windows command prompt
# MINSPACES : Minimum spaces between printed numbers
# MAXSPACES : Maximum spaces between printed numbers
WIDTH = 80
MINSPACES = 1
MAXSPACES = 5


def helper_maxdigit(low, high):
    '''Return the max digit of the number in [low,high].

    This function is mainly used to help print_randoms().
    In this function, - perator is also counted.
    As int type object cannot use len(), convert arguments to str type.
    Then determine the max digit by comparing len(str(low)) and len(str(high)).
    The higher value between len(str(low)) and len(str(high)) is determined
    by maxdigit. And return the maxdigit.

    :param low: the lowest value when determining the range of numbers.
    :type low:  int

    :param high: the highest value when determining the range of numbers.
    :type high:  int

    :return: length of the one with the longest length
             between the lowest value and the highest value.
    :rtype:  int

    example:
        low: -100  high: 10   returns 4
        low: -10   high: 100  returns 3
    '''
    # If low is longer than high.
    if len(str(low)) > len(str(high)):
        maxdigit = len(str(low))

    # If low is shorter than or equal to high.
    else:
        maxdigit = len(str(high))
    return maxdigit


def helper_nspaces(maxdigit, cols):
    '''Calculate how many nspaces(=whitespaces) is needed between numbers and
    return the whitespaces as much as needed.

    This is the function which is made to help print_ranodms().
    The needed space for pretty one line:
        maxdigit * cols + defalut_nspaces * (cols - 1).
    Increase number of nspaces(=nspaces_num) one by one comparing with WIDTH.
    And find the number of nspaces which is nearest to 5.
    But, if (maxdigits*cols + (cols - 1)) > WIDTH, nspaces_num = 1
    After find the numbers of nspaces, return the compilation of whitespaces.

    :param maxdigit: number of digits required to print the longest number
                     in range.
    :type maxdigit:  int

    :param cols: the number of printed numbers in one line.
    :type cols:  int

    :return: compilation of calculated whitespaces.
    :rtype:  str

    :precondition:
        The following constants should be defined:
            MINSPACES:
                minimum number of nspace
            MAXSPACES:
                maximum number of naspaces
            WIDTH:
                maximum number of characters that can be printed on one line

    example:
        maxdigit: 3   cols: 4  returns '     '
        maxdigit: 12  cols: 7  returns ' '
    '''
    # Start with one digit by default value and gradually increase it nearby 5.
    nspaces_num = MINSPACES

    # Check wheter the line to be printed is longer than WIDTH.
    if maxdigit * cols + nspaces_num * (cols - 1) > WIDTH:
        # As line is longer than WIDTH, nspaces_num is MINSPACES.
        pass

    # With default value of nspaces_num, line is shorter than WIDTH.
    else:
        #
        # Increase nspaces_num until the first moment when calculation value is
        # bigger than WIDTH, and then use the (nspaces_num - 1) which is the
        # greatest value smaller than WIDTH.
        #

        # Find the first moment when calculation value is bigger than WIDTH.
        while MINSPACES <= nspaces_num <= MAXSPACES:
            if maxdigit * cols + nspaces_num * (cols - 1) > WIDTH:
                break
            # Increase nspaces_num to make it nearby 5.
            nspaces_num += 1

        # Subtract 1 to make the greatest calculation value smaller than WIDTH.
        nspaces_num -= 1

    return ' ' * nspaces_num


def print_randoms(low, high, total, cols):
    """Randomly print the 'total' number between low and high.
    Print 'cols' number in one line and lastly print average of those numbers.

    This function has no return value.
    This function use helper_maxdigit() function and help_nsapces() function.
    helper_maxdigit() function to find the maximum number of digits between
    low and high.
    helper_nspaces() to determine the number of whitespaces between numbers.
    The number as many as the columns will be printed with spaces between them.
    If we do total/cols, the portion is the number of full-cols line and
    the remainder is the number of integers we will print in last line.
    As the number of integers in last line and other lines can be different,
    a separate method for printing the last line is made.
    Also, to print the average of integers in last line, variable sums is
    assigned to zero, and add the integer to the sums each time when random
    integer is selected.

    :param low: the lowest number in the range.
    :type low:  int

    :param high: the highest number in the range.
    :type high: int

    :param total: the number of integers you want to print.
    :type total:  int

    :param cols: the number of integers which is printed in one line.
    :type cols:  int

    :return: none

    :precondition:
        The following module should import:
            random module

        The following definition should be defined first:
            helper_maxdigit()
            helper_nspaces()

    :constraint:
        total >= cols
    """
    # Find maxdigit(number of max digits from low to high) and
    # nspaces(whitespaces between the numbers) using other functions.
    maxdigit = helper_maxdigit(low, high)
    nspaces = helper_nspaces(maxdigit, cols)

    # Set variable sums to caluculate average later.
    sums = 0

    #
    # Print numbers except final line.
    #

    # variable line means the number of line you print.
    # It will increase one by one if one line print is complete.
    line = 1

    # while loop for full-cols lines.
    while line <= int(total//cols):
        # variable count means how many numbers are printed in one line.
        # If one line is finished to print, count is initialized to 1.
        count = 1

        # while loop for print one line.
        while True:
            # Select random integer range from low to high.
            num = random.randint(low, high)
            # Sum that integer to calculate average later.
            sums += num

            # Print one integer aligned to the right of the maxdigit size.
            # The line does not change to have nspaces behind printed integer.
            print('{:{n}}'.format(num, n=maxdigit), end='')

            # Check if all integers are printed in one line.
            if count == cols:
                # Go to next line.
                print('')
                break

            # nspaces are attached to the back of printed integers,
            # but they do not change the line to have integer behind.
            print(nspaces, end='')
            # As one more integers will be printed, plus one to count.
            count += 1

        # Plus one to print next line.
        line += 1

    #
    # Print last line.
    #

    # Reset the variable count to count the number of last line's integer.
    # It wil increase one by one if one integer is printed.
    count = 1

    # Loop until integers of remainder number are printed.
    while count <= int(total % cols):

        # Select random integer range from low to high.
        num = random.randint(low, high)
        # Sum that integer to calculate average later.
        sums += num

        # Print one integer aligned to the right of the maxdigit size.
        # The line does not change to have nspaces behind printed integer.
        print('{:{n}}'.format(num, n=maxdigit), end='')

        # Check if all integers are printed.
        if count == int(total % cols):
            # Finish printing the integers.
            print('')
            break

        # nspaces are attached to the back of printed integers,
        # but they do not change the line to have integer behind.
        print(nspaces, end='')
        # As one more integers will be printed, plus one to count.
        count += 1

    # Print the average in decimal two points.
    print('Average : {:.2f}'.format(sums/total))

# -- end of 2020313793.정우성.HW3.py
