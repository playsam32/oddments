#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 민형복, All rights reserved.
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW9.py
#  Written on : May. 25, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-08, 'Classes' program
#
#  Modification History:
#     * version 1.0, by 정우성, May. 25, 2020
#       - 1st released on this day.
#  end of Modification History
#

"""A module for 9th lab for practicing 'Classes'

This is a module for practicing 'Classes'. One class 'Poly' are packed here.
With this class, you can control polynomial about coefficient.
Simple task, such as sum the coefficient or append new coefficient in data.

Class:
    Poly : Polynomial as a composition of dict.

For simple example:
    obj = Poly({1:2, 2:3}
    obj.append(-3,3)
    print(obj); {1:2, 2:3, 3:-3}

All elements in parameter should be numeric.
You can even sum coeffient, and find out coefficient corresponding to exponent.
For more details, please check each methods in class Poly.
"""


class Poly:
    """Polynomial as a composition of dict.

    Public method in Poly:
    poly()     : method that return the polynomial as a dict.
    tuplelist(): Get polynomial as a list of (coefficient, exponent) tuples.
    get_coeff(): Get coefficient of exponent.
    append()   : append a new data in coefficeint and exponent if exponent
                 does not exist in data. Then return True/False  wheter done.
    add()      : append a new data if exponent does not exist in data.
                 If does, sum conefficient in already existing coefficient.

    Class poly does not have subclass.
    You can make poly obeject with "obj = Poly(dic or 2-tuples)"
    You can enter nothing in parameter cause it has default value '{}'.
    Here, 2-tuples means the list of tuples with numer pair.
    For example:
        obj = Poly()
        obj = Poly({1:2, 2:3})
        obj = Poly([(1,2), (2,3)])

    Above public method do not change the orignal list or dictinary because
    those method control the copys.
    For more details, please check each methods.
    """

    def __init__(self, d={}):
        """Initializer of Poly class.

        Check if elements in d satisfying the precondintions.
        If d is list_of_2-tuples, convert that to dictinary.
        If d is dictionary, copy that. Then name those data '_polydata'.

        :param d: Data that express polynomial
                  Default : empty dictionary
                  if type(d) == dictionary : {exponent: conefficient,}
                  if type(d) == list       : [(coefficient, exponent),]
        :type d: dictionary
                 list

        :precondition: elements in data(d) should be numeric.
        """
        if type(d) == dict:
            # exponents are keys in dict
            for expon, coeff in d.items():
                assert type(expon) == int, 'exponents (keys) shall be int'
                assert type(coeff) in (int, float), \
                    'coefficients (values) shall be int or float'

            # we allow destroying d after this call.
            self = d.copy()
        else:
            # iterable of 2-tuples: coefficients comes first.
            assert self._iterable(d), 'argument shall be either dict or list.'
            assert all(len(item) == 2 for item in d), \
                'list argument shall be a list of 2-tuples.'
            for coeff, expon in d:
                assert type(expon) == int, \
                    'exponents (2nd ele) shall be int'
                assert type(coeff) in (int, float), \
                    'coefficients (1st ele) shall be int or float'

            # change order since expon's are keys.
            self = dict((expon, coeff) for coeff, expon in d)

    def _iterable(self, obj):
        """Helper method to check if given object is iterable.

        This method checks if given object "obj" is iterable or not.
        FYI, you may use isinstance(obj, Iterable) defined at collections.abc.

        :param obj: We check if this "obj" is iterable or not.
        :type obj: any

        :returns: True if "obj" is iterable, False otherwise.
        :rtype: bool
        """
        try:
            iter(obj)
        except TypeError:
            return False
        else:
            return True

    def __str__(self):
        """str() function.

        Return the form of data that you entered when construct the class.
        Use print() to use these method.

        :returns: form of self
        :rtype:   str
        """
        return f'{self}'

    def __repr__(self):
        """repr() function.

        Return the information of data when construct the class.
        Use repr() to use these method."""
        return f'{self.__class__.__name__}({self})'

    def __len__(self):
        """len() function.

        Return the lenght which means how many terms data has

        :returns: the number of terms that data contains
        :rtype:   int
        """
        return len(self)

    def poly(self):
        """method that return the polynomial as a dict.

        If user want to get data of polynomial, he should use this method than
        access the instance variable instead.

        :return: polynomial as a dict
        :rtype:  dict
        """
        return self

    def tuplelist(self):
        """Get polynomial as a list of (coefficient, exponent) tuples.

        Make a list_of_2-tuples which convert polydata(dictionary).
        Returns polynomial as a list of (coeff, expon) tuples.

        :return: a list of (coeff, expon) tuples
        :rtype: list
        """
        poly_as_tuples = []
        for exponent in self:
            coeff = self[exponent]
            poly_as_tuples.append((coeff, exponent))
        return poly_as_tuples

    def get_coeff(self, exponent):
        """Get coefficient of exponent.

        Get coefficient of exponent in form of list_of_2-tupels.
        Regardless whether exponent is iterable or int, check if exponent is in
        the self. If do, pair exponent with that coefficient.
        If not, pair exponent with 0. Than return the list of pairs which known
        as list_of_2-tuples

        :param exponent: one or more exponent.
        :type exponent:  int or iterable(such as list, tuple etc..)

        :returns: list_of_2-tuples that pair (coefficient, exponent)
        :rtype:   list

        :precondition: elements in exponents should be numeric
        """
        assert (self._iterable(exponent) or type(exponent) == (int or float)),\
            repr(exponent) + 'does not satisfy the precondition'

        r_list = []
        if self._iterable(exponent):
            for num in exponent:
                assert type(num) == (int or float),\
                    repr(num) + 'is not numeric.'
                try:
                    r_list.append((self[num], num))
                except KeyError:
                    r_list.append((0, num))
            return r_list

        elif type(exponent) == int:
            try:
                r_list.append((self[exponent], exponent))
            except KeyError:
                r_list.append((0, exponent))
            return r_list

    def append(self, coefficient, exponent):
        """append a new data in coefficeint and exponent if exponent does not
        exist in data. Then return True/False  wheter done.

        Check coefficient and exponent are iterable or integer. Then check if
        exponent exist in data(self). If exist, return False.
        If does not exist, append the (coefficient, exponent) in data. But if
        coefficient is 0 or 0.0, the (coefficient, exponent) is never appended.
        After all new data is appended, return True. If coefficient has more
        elements than exponent, do not use the elements of coefficient after
        len(exponent)_index.

        :param coefficient: package of coefficient that appended in data
        :type coefficient:  int or iterable(list, tuple etc...)

        :param exponent: package of exponent that appended in data
        :type exponent:  int or iterable(list, tuple etc...)

        :returns: True if exponent do not exist in data.
                  Flase if exponent do exist in data.
        :retype: boolean

        :precondition: elements in coefficient and exponent should be numeric.
        """
        assert type(coefficient) == (int or float)\
            or self._iterable(coefficient), \
            f'{repr(coefficient)} does not satisfy the precondition.'
        assert type(exponent) == (int or float) or self._iterable(exponent), \
            f'{repr(exponent)} does not satisfy the precondition.'

        # If exponent is iterable.
        if self._iterable(exponent):

            # convert sequence to list for convenient coding.
            exponent = list(exponent)
            for item in exponent:
                assert type(item) == (int or float), \
                    'There are non number in exponent.'
            # If coefficient is iterable.
            if self._iterable(coefficient):
                # Convert sequence to list for convenient coding.
                coefficient = list(coefficient)
                for item in coefficient:
                    assert type(item) == (int or float), \
                        'There are non number in coefficient.'
                assert len(coefficient) >= len(exponent), \
                    'coefficient should be equal or longer than exponent.'

                # main loop for append.
                for index in range(len(exponent)):
                    if exponent[index] in self:
                        return False
                    elif coefficient[index] == 0:
                        pass
                    else:
                        self[exponent[index]] = coefficient[index]
                return True

            # type(coefficient) == int
            else:
                assert len(exponent) == 1, \
                    'coefficient has too many elements than exponent'
                if not coefficient:
                    pass
                else:
                    if exponent[0] in self:
                        return False
                    else:
                        self[exponent] = coefficient
                        return True

        # type(exponent) == int
        else:
            # If coefficient is iterable.
            if self._iterable(coefficient):
                coefficient = list(coefficient)
                assert len(coefficient) >= 1,\
                    f'{coefficient} is empty!'

                if exponent in self:
                    return False
                else:
                    if not coefficient[0]:
                        return True
                    self[exponent] = coefficient[0]
                    return True

            # type(coefficient) == int
            else:
                if not coefficient:
                    return True
                else:
                    if exponent in self:
                        return False
                    else:
                        self[exponent] = coefficient
                        return True

    def add(self, coefficient, exponent):
        """append a new data if exponent does not exist in data. If does, sum
        conefficient in already existing coefficient.

        Check coefficient and exponent are iterable or integer. Then check if
        exponent exist in data(self). If exist, sum pairing
        coefficient in already existing coefficient in data.
        If does not exist, append the (coefficient, exponent) in data. But if
        coefficient is 0 or 0.0, the (coefficient, exponent) is never appended.
        If coefficient has more elements than exponent, do not use the elements
        of coefficient after len(exponent)_index.

        :param coefficient: package of coefficient that appended in data
        :type coefficient:  int or iterable(list, tuple etc...)

        :param exponent: package of exponent that appended in data
        :type exponent:  int or iterable(list, tuple etc...)

        :returns: none
        :rtyoe:   none

        :precondition: elements in coefficient and exponent should be numeric.
        """
        assert type(coefficient) == (int or float)\
            or self._iterable(coefficient), \
            f'{repr(coefficient)} does not satisfy the precondition.'
        assert type(exponent) == (int or float) or self._iterable(exponent), \
            f'{repr(exponent)} does not satisfy the precondition.'

        # If exponent is iterable
        if self._iterable(exponent):

            # convert sequence to list for convenient coding.
            exponent = list(exponent)
            for item in exponent:
                assert type(item) == (int or float), \
                    'There are non number in exponent'
            # If coefficient is iterable
            if self._iterable(coefficient):
                # Convert sequence to list for convenient coding.
                coefficient = list(coefficient)
                for item in coefficient:
                    assert type(item) == (int or float), \
                        'There are non number in coefficient'
                assert len(coefficient) >= len(exponent), \
                    'coefficient should be equal or longer than exponent.'

                # Check if exponents are already in exponent
                for index in range(len(exponent)):
                    if exponent[index] in self:
                        self[exponent[index]] += coefficient[index]
                # if there are 0 in coefficient, pass
                    elif coefficient[index] == 0:
                        pass
                    else:
                        self[exponent[index]] = coefficient[index]
            # type(coefficient) == int
            else:
                assert len(exponent) == 1, \
                    'coefficient has too many elements than exponent'
                if not coefficient:
                    pass
                else:
                    if exponent[0] in self:
                        self[exponent[0]] += coefficient
                    else:
                        self[exponent[0]] = coefficient

        # type(exponent) == int
        else:
            # If coefficient is iterable
            if self._iterable(coefficient):
                coefficient = list(coefficient)
                assert len(coefficient) >= 1,\
                    f'{coefficient} is empty!'

                if not coefficient[0]:
                    pass
                elif exponent in self:
                    self[exponent] += coefficient[0]
                else:
                    self[exponent] = coefficient[0]

            # type(coefficient) == int
            else:
                if not coefficient:
                    pass

                elif exponent in self:
                    self[exponent] += coefficient
                else:
                    self[exponent] = coefficient

# -- end of 2020313793.정우성.HW9.py
