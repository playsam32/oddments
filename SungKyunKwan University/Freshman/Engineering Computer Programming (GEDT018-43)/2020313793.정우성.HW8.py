#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW8.py
#  Written on : May. 18, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-08, 'Dictionaries & Sorting' program
#
#  Modification History:
#     * version 1.0, by 정우성, May. 18, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""A module for 8th lab for practicing 'Dictionaries & Sorting'

This module is made to practice 'Dictionaries & Sorting'. So even there are
more useful 'Counter' class for sorting, we do not used them and sort the
dictionary primitively.
This module contains 3 functions. One main function and two helper functions.
Main Function:
    sort_freq(): return the filesize, number of characters and pair in tuple of
                 character and frequency of each in text file into list with
                 sorting.
Helper function:
    -These functions are made to use 'sort' method smartly.
    keyfunc_0(): return the first element
    keyfunc_1(): return the second element
For more details for each functions, please check each functions' docstring.

Note: In function sort_freq(), we open text file with 'UTF-8' encoding.
"""


def keyfunc_0(pair):
    """helper functions for sort_freq()

    If pair data(here is the tuple in list which converted from dictionary) is
    inputed, return the first element of that. This function is made to help
    sort_freq() so its type of parameter and return is designated.

    :param pair: pair data which is converted from dictinoary
    :type pair:  tuple

    :returns: first element in data
    :rtype:   str
    """
    assert type(pair) == tuple,\
        repr(pair) + 'is not tuple pair'

    return pair[0]


def keyfunc_1(pair):
    """helper functions for sort_freq()

    If pair data(here is the tuple in list which converted from dictionary) is
    inputed, return the second element of that. This function is made to help
    sort_freq() so its type of parameter and return is designated.

    :param pair: pair data which is converted from dictinoary
    :type pair:  tuple

    :returns: second element in data
    :rtype:   int
    """
    assert type(pair) == tuple,\
        repr(pair) + 'is not tuple pair'

    return pair[1]


def sort_freq(filename):
    """return the filesize, number of characters and pair in tuple of character
    and frequency of each in text file into list with sorting.

    Open the textfile with 'UTF-8' encoding. Read the text file line by line
    and then check filesize, number of each characters in file.
    Then return the filesize, number of characters in file and dictionary
    whose elements are character-frequency pairs.
    return dictionart is sorted twice. First sorted by first element in pair
    and second sorted by second element in pair. Then dictionary is sorted by
    frequency in ascending, and if there are same frequency, sorted those
    by the unicode number also in ascending

    :param filename: name of the file from which the information will be
                     extracted.
    :type filename: str

    :returns: 3-tuple; (filesize, num_chars, dlist),
              where
              filesize: size of the ''filename'' as total number of characters
                        read from file.
              num_chars: number of unique characters in the file.
              dlist: list of 2-tuples, [(c1, n1), (c2, n2), (c3, n3), ...],
                     where
                     c1, c2, ... = each character in the given file,
                     n1, n2, ... = frequencies of occurrences of the
                                   characters.
    :rtype: 3-tuple of (int, int, list)

    :precondition:
        input file should be text file.
    """
    assert type(filename) == str,\
        repr(filename) + 'is not string.'

    fobj = open(filename, 'r', encoding='UTF-8', newline='')

    # file size will check with adding characters line by line.
    # sample_dic will be added characters or plus frequency.
    file_size = 0
    sample_dic = {}

    for line in fobj:
        file_size += len(line)
        for char in line:
            # Character readily exists.
            if char in sample_dic:
                sample_dic[char] += 1
            # Character added first.
            else:
                sample_dic[char] = 1

    num_chars = len(sample_dic)
    # Convert dic to list for sorting.
    char_list = list(sample_dic.items())

    char_list.sort(key=keyfunc_0)
    char_list.sort(key=keyfunc_1)

    return file_size, num_chars, char_list

# -- end of 2020313793.정우성.HW8.py
