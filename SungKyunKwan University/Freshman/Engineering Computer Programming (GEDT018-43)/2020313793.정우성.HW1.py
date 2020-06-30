#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW1.py
#  Written on : Mar. 25, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-01, 'print() and String Formatting' program
#
#  Modification History:
#     * version 1.0, by 정우성, Mar. 25, 2020
#       - 1st released on this day.
#  end of Modification History
#
""" Same sentences will be printed by using 4 differet methods.
4 diffrent methods are
1. Using print() function without using string formatting.
2. Using 'f-string' for string formatting.
3. Using 'string'.format() for string formatting.
4. Using 'string'%(tuple) for string formatting.
The following senteces will be printed 4 times:

---(Explanation of which method are used)---
My name is 정우성, and id number is 2020313793
r = 2.00 ('r = 2.0' will be printed for the first case.)
area = 12.57 ('area = 12.566370614359172' will be printed for the first case.)
"""
#
# Import math module to use pi for computing area of circle.
#

import math

#
# Assigning the radius and computing the area of circle to use them in print
# functions.
#
radius = 2.0
square = radius * radius
area_of_circle = math.pi * square

#
# Assingning name and ID number to use them in print functions.
#
name = '정우성'
id_number = 2020313793

#
#  (1) Only using print()
#

print('--- Using print() without string formatting ---')
# sep = '' is used to paste '정우성(name)' and ','.
print('My name is ', name, ', and id number is ', id_number, sep='')
print('r =', radius)
# '\n' is used for the spaces between paragraphs.
print('area =', area_of_circle, '\n')

#
#  (2) f-string
#

print(f'--- Using f-string ---')
print(f'My name is {name}, and id number is {id_number}')
# {:.2f} is used to print in float type under two decimal places.
print(f'r = {radius:.2f}')
# '\n' is used for the spaces between paragraphs.
print(f'area = {area_of_circle:.2f} \n')

#
#  (3) str.format()
#

# Nothing is substituted because round bracket is empty.
print('--- Using str.format() ---'.format())
# 'name' is substituted in '0', and 'id_number'is substituted in '1'.
print('My name is {0}, and id number is {1}'.format(name, id_number))
print('r = {:.2f}'.format(radius))
# area_of_circle is assigned as 'S', so {S:.2f} is same with {:.2f}.
# Also, '\n' is used for the spaces for paragraphs.
print('area = {S:.2f} \n'.format(S=area_of_circle))

#
#  (4) str % (tuple or dict)
#

# '%%' means a single % character. And nothing is substituted here.
print('--- Using %% (tuple) ---' % ())
print('My name is %s, and id number is %d' % (name, id_number))
print('r = %.2f' % radius)
print('area = %.2f' % (area_of_circle,))

# -- end of 2020313793.정우성.HW1.py
