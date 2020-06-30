#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW6.py
#  Written on : May. 03, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-06, 'Lists & Sorting Basics' program
#
#  Modification History:
#     * version 1.0, by 정우성, May. 03, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""A module for 6th lab for practicing 'list' and numeric example.

Whole 10 functions are difined. 6 functions are related to list and
other 4 functions are related to numeric example.
6 functions which related to list:
    sum_list():
        Return the sum of elements in list.
    numberof():
        Return the number of times specific value occurs in list.
    replace():
        Return the copylist with modifing the specific value.
    remove_dups():
        Return the copylist removing the adjacent duplicates.
    remove_first():
        Return the copylist that removes the specific value if it exist.
    sort_list():
        Sort the given list upward or downward.

4 functions which related to numeric example:
    sum_to():
        Return the sum from 1 to given number.
    num_digits():
        Return the digits of given number.
    sum_digits():
        Return the sum of each digit of given number.
    into():
        Return the number of times given number can divide other given number.

These functions are made without using iterations(for-loops), dictionaries,
or classes. But made with methods for list, strings.
For more details about each functions, please check each functions' docstring.
"""


def sum_list(thelist):
    """Return the sum of elements in list.

    Sum all the elements in list. This function does not use 'sum' method.
    In this function, sum the elements one by one and return the sum.
    But if argument is empty list, return 0.

    :param thelist: the list to sum
    :type thelist:  list

    :returns: the sum of the integers in list.
    :rtype:   int

    :precondition:
        'thelist' is a list of ints

    :Example:
        sum_list([34]) is 34
        sum_list([7,34,1,2,2]) is 46
    """
    assert type(thelist) == list,\
        repr(thelist) + ' is not list.'
    index = 0
    while not index == len(thelist):
        assert type(thelist[index]) == int, \
            repr(thelist[index]) + ' is not int.'
        index += 1

    # Blank list returns 0.
    if len(thelist) == 0:
        return 0
    else:
        # Reset the index as variable 'index' used above.
        index = 0
        sum_value = 0
        while not index == len(thelist):
            sum_value += thelist[index]
            index += 1
        return sum_value


def numberof(thelist, value):
    """Return the number of times value occurs in thelist.

    Count how many values are appear in thelist.
    This function use count method in list object and return that.

    :param thelist: the list to count.
    :type thelist:  list

    :param value: the value to count
    :type value:  int

    :returns: the number of times value occurs in thelist.
    :rtype:   int

    :precondition:
        'thelist' is a list of ints
    """
    assert type(thelist) == list,\
        repr(thelist) + ' is not list.'
    index = 0
    while not index == len(thelist):
        assert type(thelist[index]) == int, \
            repr(thelist[index]) + ' is not int.'
        index += 1
    assert type(value) == int, repr(value) + ' is not integer.'

    # Reset the index as variable 'index' used above.
    index = 0
    count_value = 0
    while not index == len(thelist):
        if thelist[index] == value:
            count_value += 1
        index += 1

    return count_value


def replace(thelist, from_value, to_value):
    """Return the copylist with modifing the 'from_value' to 'to_value'.

    Copy the thelist and replace all 'from_value' to 'to_value'
    if 'from_value' is contained in copy list. Then return the copied list.
    Original list is not modified.

    :param thelist: The list to search ``from_value`` from
    :type thelist:  list

    :param from_value: The value to replace
    :type from_value:  int

    :param to_value: The value to replace with
    :type to_value:  int

    :returns: a COPY of thelist but with all occurrences of ``from_value``
              replaced by ``to_value``.
    :rtype:   list

    :precondition:
        'thelist' is a list of ints

    Example:
        replace([1,2,3,1], 1, 4) = [4,2,3,4].
    """
    assert type(thelist) == list,\
        repr(thelist) + ' is not list.'
    index = 0
    while not index == len(thelist):
        assert type(thelist[index]) == int, \
            repr(thelist[index]) + ' is not int.'
        index += 1
    assert type(from_value) == int, \
        repr(from_value) + 'is not int.'
    assert type(to_value) == int, \
        repr(to_value) + ' is not int.'

    # Make new copy list not to modify original list.
    copy_thelist = thelist[:]
    index = 0
    while not index == len(copy_thelist):
        if copy_thelist[index] == from_value:
            copy_thelist[index] = to_value
        index += 1

    return copy_thelist


def remove_dups(thelist):
    """Return the new list removing the adjacent duplicates if they are equal.

    Make new empty list. Then append first element in original list.
    Comparing the last element in new list and next element in original list.
    If they are same, nothing happend. If they are different, append element
    to new list. Then compare with another next element in original list.
    Repeat these steps until last element is compared

    Note: 'thelist' would not be modified

    :param thelist: The list to search duplicates
    :tyoe thelist:  list

    :returns: a COPY of thelist with adjacent duplicates removed.
    :rtype:   list

    :precondition:
        'thelist' is a list of ints

    :Example:
        for thelist = [1,2,2,3,3,3,4,5,1,1,1]
        the answer is [1,2,3,4,5,1]
    """
    assert type(thelist) == list,\
        repr(thelist) + ' is not list.'
    index = 0
    while not index == len(thelist):
        assert type(thelist[index]) == int, \
            repr(thelist[index]) + ' is not int.'
        index += 1

    # Case of empty list.
    if len(thelist) == 0:
        return []
    else:
        # Reset the index as variable 'index' used above.
        index = 0
        new_list = []
        # Append first element of original list to make defalut for comparing.
        new_list.append(thelist[index])
        while not index == len(thelist):
            # last index number of new_list
            new_index = len(new_list) - 1
            if new_list[new_index] != thelist[index]:
                new_list.append(thelist[index])
            index += 1

        return new_list


def remove_first(thelist, value):
    """Return the new list that removes the first value if it is in thelist.

    Copy thelist. Then check if thelist have 'value' as a element.
    If it does, delete the first 'value' in copylist. And return thw copylist.

    Note: 'thelist' would not be modified.

    :param thelist: the list to search
    :type thelist:  list

    :param value: the value to search for
    :type value:  int

    :returns: a COPY of thelist but with the FIRST occurrence of
              ``value`` removed (if present).
    :rtype:   list

    :precondition:
        'thelist' is a list of ints
    """
    assert type(thelist) == list,\
        repr(thelist) + ' is not list.'
    index = 0
    while not index == len(thelist):
        assert type(thelist[index]) == int, \
            repr(thelist[index]) + ' is not int.'
        index += 1
    assert type(value) == int, repr(value) + ' is not integer.'

    # Make new copy list not to modify original list.
    new_list = thelist[:]
    try:
        new_list.remove(value)
    except ValueError:
        # Error raising means there is no 'value' in 'thelist'.
        pass

    return new_list


def sort_list(thelist, increasing=True):
    """sort the given list upward or downward.

    Sort thelist upward or downward. thelist is sorted in increasing order
    if increasing is 'True', the list is sorted in decreasing order
    if increasing is 'False'. defualt value of increasing is 'True'

    :Note: 'thelist' would be modified.

    :param thelist: the list to be sorted
    :type thelist:  list

    :param increasing: 'True' for increasing order
                       'False' for decreasing order
                       'True' is the default value
    :type increasing:  boolean

    :returns: nothing (None).
    :rtype:   NoneType

    :precondition:
        'thelist' is a list of ints
    """
    assert type(thelist) == list,\
        repr(thelist) + ' is not list.'
    index = 0
    while not index == len(thelist):
        assert type(thelist[index]) == int, \
            repr(thelist[index]) + ' is not int.'
        index += 1
    assert type(increasing) == bool, \
        repr(increasing) + ' is not boolean type.'

    thelist.sort(reverse=not increasing)


def sum_to(integer):
    """Sum from 1 to 'integer', and then return that value.

    Make sum_element starting from 1. Then sum the sume_element in to value
    until sum the sum_element is equal integer and sum that into value.

    :param integer: the number upto this integer is added.
    :type integer:  int

    :returns: the sum of numbers 1 to ``integer``.
    :rtype:   int

    :Example:
        sum_to(3) = 1+2+3     = 6
        sum_to(5) = 1+2+3+4+5 = 15

    :precondition:
        'integer' >= 1
    """
    assert type(integer) == int, \
        repr(integer) + ' is not int.'
    assert integer >= 1, \
        repr(integer) + ' is not equal or greater than 1.'

    # Starting value of sum element.
    sum_element = 1
    value = 0
    while not sum_element == integer+1:
        value += sum_element
        sum_element += 1

    return value


def num_digits(integer):
    """Return how many decimals the 'integer' have.

    As int type cannot use len() function, convert integer into str type.
    Then use len() method to know digits. Then return that value.

    :param integer: the number to analyze
    :type integer:  int

    :returns: the number of the digits in the decimal representation of
              'integer'.
    :rtype:   int

    :Example:
        num_digits(0) = 1
        num_digits(3) = 1
        num_digits(34) = 2
        num_digits(1356) = 4

    :precondition:
        'integer' >= 0, and it is an int
    """
    assert type(integer) == int, \
        repr(integer) + ' is not int.'
    assert integer >= 0, \
        repr(integer) + ' is not equal or greater than 0.'

    # Convert 'integer' to string for len() function.
    integer = str(integer)
    value = len(integer)

    return value


def sum_digits(integer):
    """Sum the digits in each decimal and return that.

    As integer type cannot use method liek index(), convert 'integer' into
    str type. Then slice each index and convert it into int and sum them.

    :param integer: the number to analyze
    :type integer:  int

    :returns: the sum of the digits in the decimal representation of integer.
    :rtype:   int

    :precondition:
        'integer' >= 0

    :Example:
        sum_digits(0) = 0
        sum_digits(3) = 3
        sum_digits(34)  = 3 + 4     = 7
        sum_digits(345) = 3 + 4 + 5 = 12
    """
    assert type(integer) == int, \
        repr(integer) + ' is not int.'
    assert integer >= 0, \
        repr(integer) + ' is not equal or greater than 0.'

    # Convert 'integer' to string for len() function.
    integer = str(integer)
    all_index = len(integer)

    index = 0
    sum_value = 0
    while index != all_index:
        fixed_integer = int(integer[index])
        sum_value += fixed_integer
        index += 1

    return sum_value


def into(integer, divisor):
    """Return the value that when integer is divided by divisor, how may times
    the remainder is 0.

    Divide integer into divisor. If remain is 0, divide quotient into divisor.
    Repeat that until remain is not 0.
    And whenever the remain is 0, increase the count_value one by one.
    And then return the count_value

    :param integer: the number to analyze
    :type integer:  int

    :param divisor: the number to divide by
    :type divisor:  int

    :returns: the number of times that ``divisor`` divides ``integer``,
    :rtype:   int

    :precondition:
        integer >= 1
        divisor >  1

    :Example:
        into(5,3) = 0
        into(3*3*3*3*7,3) = 4
    """
    assert type(integer) == int, \
        repr(integer) + ' is not int.'
    assert integer >= 1, \
        repr(integer) + ' is not equal or greater than 1.'
    assert type(divisor) == int, \
        repr(divisor) + ' is not int.'
    assert divisor > 1, \
        repr(divisor) + ' is not greater than 1.'

    # Increase whenever 'integer' is divided by 'divisor'.
    count_value = 0
    while True:
        if integer % divisor == 0:
            count_value += 1
            integer = integer//divisor
        else:
            break

    return count_value

# -- end of 2020313793.정우성.HW6.py
