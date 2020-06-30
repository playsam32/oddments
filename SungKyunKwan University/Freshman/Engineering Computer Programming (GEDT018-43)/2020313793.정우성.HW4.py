#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW4.py
#  Written on : April. 20, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-04, 'Objects' program
#
#  Modification History:
#     * version 1.0, by 정우성, Apr. 20, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""Module that contains function readwrite() which print current time and
infile's information pretty in outfile and shell.

In this module, only one function, readwrite() exist. readwrite function offers
current time data, grades about students, and average age of students.
This function is built to use textfile in infile and outfile.
--Simple steps of readwrite() function--
First, print current time in 12-hour-format in first line.
Then, print students' information pretty which in infile.
Lastly, print average age of students.
"""

# Import datetime module to process date and time, and eepy for 2 functions.
from datetime import datetime
from eepy import number_of_words, get_word


def readwrite(infile, outfile):
    """Print current time and infile's information pretty in outfile and shell.

    Before start, notify that in this paragraph, 'print' means that printing
    to shell and outfile at the same time.
    Initially, the current time is printed in 12 hour format.
    As informations in the infile, name, age, and grades, are not good to see
    each other, print them pretty with average of grades each other.
    Considering monospace font, open file using 'UFT-8' encoding and classify
    korean name and english name.
    Then, print average ages last line.

    :param infile: name of textfile which contains student's information.
                   for example, 'filename.txt'
    :type infile:  str

    :param outfile: name of textfile which will receive organized information.
                    for example, 'filename.txt'
    :type outfile: str

    :return: none
    :rtype:  none

    :precondition:
        following should be imported:
            datetime         from  datetime  module
            get_word         from  eepy      module
            number_of_words  from  eepy      module

    :constraint:
        order of infile's information:
            name, age, and grades
        legth of name:
            length of english name <= 10
            length of korean name  <= 5
        extensions of infile and outfile recommended to be txt.

    :example:
        infile text:
            정우성     21    A  A B   A   C
            정우진  24  B C   D  B   B
        outfile text and shell:
            Current time is at {Current time}
            정우성         21  A A B C A    3.40
            정우진         24  B C D B B    2.40
            Average age of the students in file = 22.50
    """
    # Open files with 'UTF-8' encoding.
    grades = open(infile, 'r', encoding='UTF-8')
    results = open(outfile, 'w', encoding='UTF-8')

    #
    # Print current time.
    #

    # Divide time from year to second and am/pm.
    now = datetime.now()

    year = now.strftime('%Y')
    month = now.strftime('%B')
    day = now.strftime('%d')
    hour = now.strftime('%I')
    minute = now.strftime('%M')
    second = now.strftime('%S')
    meridian = now.strftime('%p')

    # Separate time and date for pretty coding.
    time = f'{hour}:{minute}:{second} {meridian}'
    date = f'{month} {day}, {year}'

    # Print first line - current time.
    print(f'Current time is at {time} on {date}')
    print(f'Current time is at {time} on {date}', file=results)

    #
    # Print students' informations.
    #

    # variables for average of ages in last line.
    sum_of_age = 0
    students_nums = 0

    # Default line for while loop.
    line = grades.readline()

    while line:
        # Loop while means that the line is not blank, meaning there is one
        # more student.
        students_nums += 1
        # Indicator for how many informations are used in one line.
        word = 0

        #
        # Identify length of name.
        #

        # As (word = 0), we can get name from infile.
        name = get_word(line, word)
        name_len = 0
        name_index = 0

        # Check whether each characeter of name is Eng or Kor.
        while name_index < len(name):
            # Eng
            if 0 <= ord(name[name_index]) <= 127:
                name_len += 1
            # Kor
            elif 44032 <= ord(name[name_index]) <= 55203:
                name_len += 2
            # Next name character.
            name_index += 1

        # length of name(consider monospace font) + white space = 15
        whitespace = 15 - name_len
        part_name = get_word(line, word) + ' '*whitespace

        #
        # Identify age.
        #

        # Indicate use next information
        word += 1
        # As (word = 1), we can get age.
        sum_of_age += int(get_word(line, word))
        part_age = get_word(line, word)

        #
        # Identify grade.
        #

        # sum of grade for average grades of student.
        sum_of_grades = 0
        # Grades will be append behind.
        part_grade = ''

        # Untill last grade is used.
        while number_of_words(line) - (word+1):
            # To use next information.
            word += 1
            indi_grade = get_word(line, word)
            # Grades part will be made with white space between each other.
            part_grade += indi_grade + ' '

            # Calculate the sum of grades
            if indi_grade == 'A':
                sum_of_grades += 4.0
            elif indi_grade == 'B':
                sum_of_grades += 3.0
            elif indi_grade == 'C':
                sum_of_grades += 2.0
            elif indi_grade == 'D':
                sum_of_grades += 1.0
            elif indi_grade == 'F':
                sum_of_grades += 0.0

        # (number_of_words(line) - 2) means number of subject because there are
        # only grades information except name and age information.
        part_average = f'{sum_of_grades/(number_of_words(line) - 2):.2f}'

        #
        # print student's information pretty.
        #

        information = f'{part_name}{part_age}  {part_grade}   {part_average}'
        print(information)
        print(information, file=results)

        # Next line.
        line = grades.readline()
    #
    # Print average age of students.
    #

    average_age = f'{sum_of_age/students_nums:.2f}'
    last_line = f'Average age of the students in file = {average_age}'
    print(last_line)
    print(last_line, file=results)

    # Close files.
    grades.close()
    results.close()

# -- end of 2020313793.정우성.HW4.py
