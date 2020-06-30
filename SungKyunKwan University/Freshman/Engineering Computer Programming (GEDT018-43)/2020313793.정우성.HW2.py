#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW2.py
#  Written on : April. 05, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-02, 'Strings' program
#
#  Modification History:
#     * version 1.0, by 정우성, Apr. 05, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""Test three functions when it is executed as a script.

The three functions are:
    convert2minutes(timeofday)
    replaced_first_by_second(string)
    swap(s1,s2)
These functions were made without using 'if', 'while', and 'for'.
However, testmain(), the function to test these three functions, uses 'if',
'while', and 'for'.
If it is called as module, nothing will happen.
"""


def convert2minutes(timeofday):
    """Convert the time string of the 24-hour format to minutes since midnight.

    This function expresses the 24-hour format in minutes.
    Initially, divide by hour and minutes in str type based on ':'.
    And if hour and minute have a single digit, put a zero in front of it.
    In this way, we unify the hour and the minute into two digits.
    For example, '3' -> '03', '11' -> '11'
    And then we divide the hour and minute into the tens place and ones place.
    Then, convert each places into int type.
    And make new_hour and new_minute in int type.
    After convert hour unit to minute unit, assign the value as the sum of
    converted new_hour and and new_minute.

    :param timeofday: time of day 'H[H]:M[M]',
                      where [] means that it is optional.
    :type timeofday:  str

    :return: minutes since midnight
    :rtype:  int

    :precondition:
        timeofday should be a string of format 'H[H]:M[M]', i.e.,
        1 or 2 digit followed by ':' and followed by 1 or 2 digit.
        The 1st digit(s) are hours, and the 2nd digit(s) are
        minutes. There is no white spaces inside the string.

    :constraint:
        Do not use 'if', 'for' and/or 'while' in this function.

    :example:
        timeofday: '02:23' returns 143 (== 2*60+23)
        timeofday: '2:3'   returns 123 (== 2*60+3)
        timeofday: '2:03'  returns 123 (== 2*60+3)
        timeofday: '10:3'  returns 603 (== 10*60+3)
        timeofday: '11:13' returns 673 (== 11*60+13)
    """
    # Find where ':' is to separate the frontward(hour) and backward(minute).
    partition = timeofday.index(':')

    # Separates the hour part and minute part.
    hour = timeofday[:partition]
    minute = timeofday[partition+1:]

    # Unifies the hours and minutes into length 2 adding 0.
    # If the initial len(str) = 2, nothing happens.
    # eg. '3' -> '03', '11' -> '11'
    hour = hour.zfill(2)
    minute = minute.zfill(2)

    # Divides tens place and ones place both hour and minute.
    # And converts them into int.
    hour_tens = int(hour[0])
    hour_ones = int(hour[1])
    minute_tens = int(minute[0])
    minute_ones = int(minute[1])

    # Converts hour and minute to one integer by using tens and ones place.
    new_hour = hour_tens*10 + hour_ones
    new_minute = minute_tens*10 + minute_ones
    # Adds the hour to minutes after converting hour to the minute unit.
    value = new_hour*60 + new_minute

    return value


def second_replaced_by_first(string):
    """Return a string from a given string where the 2nd occurrence of
    its first character have been changed to '$', except the first character
    itself.

    Start by distinguishing the first spelling and the other parts of the word.
    Assign the the other parts of the word as body_part.
    Then find the index rule between string and second_occurrence.
    (you can find more deatail in line 133)
    Changes the second_occurrence in string into '$' and assign changed string
    as value. And finally, return that value.

    :param string: any string can input, even symbol and number.
    :type string:  str

    :return: string which changed 2nd occurrence into $.
    :rtype:  str

    :precondition: len(string) >= 2 and the the 2nd occurrence always exist
    :constraint: Do not use 'if', 'for' and/or 'while' in this function.

    :example:
        Sample String   : 'restart'
        Expected Result : 'resta$t'
    """
    # To find the 2nd occurrence in a word, specify the first_character.
    first_character = string[0]

    # Assign body_part which excludes string[0] from 'string'.
    # ex: string    == 'apple'
    #     body_part == 'pple'
    body_part = string[1:]

    # As body_part is equal to string without string[0],
    # body_part[n] = string[n+1].
    # Therefore, the index number of second_occurrence in string is same with
    # the (index number of second_occurrence in body_part + 1)
    second_occurrence = body_part.index(first_character) + 1

    # Changes the second_occurrence to '$' and assigns them as value in str.
    value = string[:second_occurrence] + '$' + string[second_occurrence+1:]

    return value


def swap(s1, s2):
    """Return a single string from two given strings, separated by a space and
    swap the 1st two characters of each string.

    Slice the front two digits in s1 and s2 and assign new_s1 and new_s2 which
    switch the front seats each other. After that, connect new_s1 and new_s2
    with ' ' and then assign it as value.
    Finally, return this value.
    In all of these processes, the variables are all str type.

    :param s1: any string can input, even symbol and number.
    :type s1:  str

    :param s2: any string can input, even symbol and number.
    :type s2:  str

    :return: single string which swap the 1st two characters and connect them
             with white space.
    :rtype:  str

    :precondition:
        len(s1) >= 2
        len(s2) >= 2

    :constraint: Do not use 'if', 'for' and/or 'while' in this function.

    :example:
        Sample String : 'abc', 'xyz'
        Expected Result : 'xyc abz'
    """
    # Separate 1st two characters of each string.
    particle_of_s1 = s1[:2]
    particle_of_s2 = s2[:2]

    # Make new_s1 and new_s2 with exchange each two characters.
    # ex) s1 == abc, s2 == def
    #     new_s1 == dec, new_s2 == abf
    new_s1 = particle_of_s2 + s1[2:]
    new_s2 = particle_of_s1 + s2[2:]

    # Connect new_s1 and new_s2 with ' '.
    value = new_s1 + ' ' + new_s2

    return value


# Test function
def testmain():
    """This is the function for test above three functions.

    convert2minute(timeofday) is substituted from '00:00' to '23:59'.
    second_replaced_by_first(string) is tested 4 cases.
    swap(s1, s2) is also tested 4 cases.
    Just type testmain() for test.

    :param: none

    :return: none

    :precondition: function convert2minutes(timeofday)
                   function replaced_first_by_second(string)
                   function swap(s1,s2)
                   should be defined first.
    """
    #
    # Test convert2minutes()
    #

    print('--- Testing function convert2minutes()')
    # count will increase by one if one test passed.
    count = 0
    
    # Possible timeline is from '00:00' to '23:59'
    for hours in range(0, 24):
        for minutes in range(0, 60):
            # Make the expected answer(return value) first.
            answer = 60*hours + minutes
            
            # Make timeofday(str type) which satisfies precondition.
            # timeofday looks like 'HH:MM'
            # ex) '03:12', '11:02'
            hours_test = str(hours).zfill(2)
            minutes_test = str(minutes).zfill(2)
            timeofday = f'{hours_test}:{minutes_test}'
            
            # Test whether function works well.
            if convert2minutes(timeofday) == answer:
                # Test pass
                count += 1
            else:
                # Test fail
                print(f'ERROR!: It doesn\'t satisfy {timeofday}')
    # If all test passed.
    if count == 1440:
        print('All test passed')

    #
    # Test second_replaced_by_first()
    #

    print('-- Testing function second_replaced_by_first()')
    # Reset the count. It will also increase by one if one test passed.
    count = 0
    
    # Make 4 test elements in list which satisfy precondition.
    # Also, make expected answer list to check wheter fuction works well.
    test_list = ['restart', 'u-plus', '001112', 'gg']
    answer_list = ['resta$t', 'u-pl$s', '0$1112', 'g$']
    
    # Test 4 elements.
    for indx, val in enumerate(answer_list):
        if second_replaced_by_first(test_list[indx]) == val:
            # Test pass
            count += 1
        else:
            # Test fail
            print(f'Error!, it doesn\'t satisfy {test_list[indx]}.')
    
    # If all test passed.
    if count == len(answer_list):
        print('All test passed')

    #
    # Test swap()
    #

    print('-- Testing function swap()')
    # Reset the count. It will also increase by one if one test passed.
    count = 0
    
    # Make test parameter(s1, s2) and answer for 4 tests.
    test_s1_list = ['abc', 'ab', 'a0b', '0a']
    test_s2_list = ['def', 'de', '1c', '1b']
    answer_list = ['dec abf', 'de ab', '1cb a0', '1b 0a']
    
    # Start test
    for indx, val in enumerate(answer_list):
        if swap(test_s1_list[indx], test_s2_list[indx]) == val:
            # Test pass
            count += 1
        else:
            # Test fail
            print(f'ERROR! swap({test_s1_list[indx]}, {test_s2_list[indx]} ')
    
    # If all test passed.
    if count == len(answer_list):
        print('All test passed')


# Test if executed as script.
if __name__ == '__main__':
    # Call test function.
    testmain()

# -- end of 2020313793.정우성.HW2.py
