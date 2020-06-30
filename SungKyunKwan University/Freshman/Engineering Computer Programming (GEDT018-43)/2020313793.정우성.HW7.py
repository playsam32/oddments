#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW7.py
#  Written on : May. 11, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-07, 'Iterations' program
#
#  Modification History:
#     * version 1.0, by 정우성, May. 11, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""A module for 7th lab for practicing 'Iterations', expecially for-loops.

Whole 2 functions are defined. These functions are made with for-loops to
practice itearatons, expecially for-loops.
Therefore, these module is made without using while-loops.
2 functions:
    get_fileinfo():
        Get how many lines, words, and characters are in text file.
    primes():
        Make prime number from 1 to given numbers and return them in list.
Also, these functions are devised to make run time as faster as we can.
For more details, please check each functions.

Note: In function get_fileinfo(), we open text file with 'UTF-8' encoding.
"""


def get_fileinfo(filename):
    """Get how many lines, words, and characters are in text file.

    First, open the text file with 'UTF-8'encoding. The newline character is
    preserved. Then read line by line until the final line.
    Whenever read each line, This function check the number of lines, words,
    and characters. After read last line, return the nuumber of lines, words,
    abd characters in turn in list with int type each.

    :param filename: filename with extension
                     file should be text file.
    :type filename:  str

    :returns: collection of lines, words and characters in turn in list
    :rtype:   list

    :precondition:
        input file should be text file.
    """
    assert type(filename) == str,\
        repr(filename) + 'is not string.'
    assert filename.endswith('.txt'),\
        repr(filename) + 'is not text file.'

    fobj = open(filename, 'r', encoding='UTF-8', newline='')
    # nl is the number of lines.
    # nw is the number of words.
    # nc is the number of characters including tab, newline etc...
    nl = 0
    nw = 0
    nc = 0

    for line in fobj:
        nl += 1
        nw += len(line.split())
        nc += len(line)
    fobj.close()
    return [nl, nw, nc]


def primes(n):
    """ Make prime number from 1 to given numbers and return them in list.

    This function use the 'Eratosthenes Sieve' to determine wheter it is prime
    or not. To introduce 'Eratosthenes Sieve' in short, if you want to know
    that if n is prime number, dividing n from 2 to sqrt(n)+1 is enough.
    This functoin finds the prime number from 1 to n using above method.
    Whenever find prime number, append it in list. This function only check
    odd number between 3 to n with containing 2 first as even number is always
    not a primenumber except 2. If find all prime numbers, return the prime
    number list.

    :param n: maximum range that you want to find prime number.
    :type n:  int

    :rturns: collection of prime numbers in list.
             each element is int type.
    :retype: list

    :precondition:
        n >= 1
    """
    assert type(n) == int, repr(n) + 'should be integer!'
    assert n >= 1, repr(n) + 'should be bigger or equal than 1.'

    if n == 1:
        return[]

    prime = [2]
    # As even number is not a prime except 2, only check odd number.
    for num in range(3, n+1, 2):
        # Use 'Eratisthenes Sieve'.
        for elem in range(2, int(num**(1/2)+1)):
            if not num % elem:
                break
        else:
            prime.append(num)
    return prime

# -- end of 2020313793.정우성.HW7py
