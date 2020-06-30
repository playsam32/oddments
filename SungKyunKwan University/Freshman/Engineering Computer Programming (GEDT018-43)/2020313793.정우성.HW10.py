#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 민형복, All rights reserved.
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW10.py
#  Written on : Jun. 01, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-10, 'Inheritance' program
#
#  Modification History:
#     * version 1.0, by 정우성, Jun. 01, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""A module with Poly class inherited from dict.

This is a module for practicing 'Inheritance' of class. One class 'Poly' are
packed here. 'Poly' Class inherit the 'dict'. With this class, you can control
polynomial about coefficient.
Simple task, such as append or modify the coefficient and find the pair based
on maximum or minimun coefficient and exponent.

Class:
    Poly : Polynomial inherited from dict.

    :example:
        obj = Poly({1:2, 2:3})
        obj.append(-3,3)
        print(obj); {1:2, 2:3, 3:-3}

        obj = Poly({6:2, 4:-7, 2:9, 1:2, 0:9})
        p.max_expon(); (2, 6)

All elements in parameter should be numeric.
For more details, please check each methods in class Poly.
"""


class Poly(dict):
    """Polynomial inherited from dict.

    Simple class that conatains the method which handle the coefficient and
    exponent of polynomial.
    You can make poly obeject with "obj = Poly(dic or list-of-2-tuples)"
    You can enter nothing in parameter cause it has default value '{}'.
    Here, list-of-2-tuples means the list of tuples with numer pair.
    :example:
        obj = Poly()
        obj = Poly({1:2, 2:3})
        obj = Poly([(1,2), (2,3)])

    :super class: dict

    :public method:
        poly()      : Return the data in dictionary.
        tuplelist() : Get polynomial as a list of tuples.
        get_coeff() : Get coefficient of exponent.
        append()    : append a new data in coefficeint and exponent if exponent
                      does not exist in data.
                      Then return True/False wheter done.
        add()       : append a new data if exponent does not exist in data.
                      If does, sum conefficient in already existing
                      coefficient.
        get_expon() : Get exponent in limited range.
        max_expon() : Return the 2-tuple which exponent is the biggest.
        min_expon() : Return the 2-tuple which exponent is the smallest.
        mas_coeff() : Return the list-of-2-tuples which coefficient is the
                      biggest.
        min_coeff() : Return the list-of-2-tuples which coefficient is the
                      smallest.
    """

    def __init__(self, d={}):
        """Initializer of Poly class.

        This class used dict's intializer. And do not override the _init_.
        If you leave parameter 'd' blank, empty dictionary will substituted.
        For the information of __init__ of dict, please use help(dict) and
        find __init__ method part.

        :param d: Data that express polynomial
                  Default : empty dictionary
                  if type(d) == dictionary : {exponent: conefficient,}
                  if type(d) == list       : [(coefficient, exponent),]
        :type d: dictionary
                 list
        """
        if type(d) == dict:
            # exponents are keys in dict
            for expon, coeff in d.items():
                assert type(expon) == int, 'exponents (keys) shall be int'
                assert type(coeff) in (int, float), \
                    'coefficients (values) shall be int or float'

            super().__init__(d)
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
            super().__init__((expon, coeff) for coeff, expon in d)

    def _iterable(self, obj):
        """Helper method to check if given object is iterable.

        This method checks if given object 'obj' is iterable or not.
        FYI, you may use isinstance(obj, Iterable) defined at collections.abc.

        :param obj: We check if this 'obj' is iterable or not.
        :type obj: any

        :returns: True if 'obj' is iterable, False otherwise.
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
        return f'{dict(self)}'

    def __repr__(self):
        """repr() function.

        Return the information of data when construct the class.
        Use repr() to use these method."""
        return f'{self.__class__.__name__}({self})'

    def poly(self):
        """Return the data in dictionary.

        :return: polynomial as a dict.
        :rtype:  dictionary
        """
        return dict(self)

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
        assert (self._iterable(exponent) or type(exponent) in (int, float)),\
            repr(exponent) + 'does not satisfy the precondition'

        r_list = []
        if self._iterable(exponent):
            for num in exponent:
                assert type(num) in (int, float),\
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
        exponent exist in self(data). If exist, return False.
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
        assert type(coefficient) in (int, float)\
            or self._iterable(coefficient), \
            f'{repr(coefficient)} does not satisfy the precondition.'
        assert type(exponent) in (int, float) or self._iterable(exponent), \
            f'{repr(exponent)} does not satisfy the precondition.'

        # If exponent is iterable.
        if self._iterable(exponent):

            # convert sequence to list for convenient coding.
            exponent = list(exponent)
            for item in exponent:
                assert type(item) == (int or float), \
                    'There are non number in exponent.'

            #
            # exponent is iterable.
            # coefficient is iterable.
            #
            if self._iterable(coefficient):
                # Convert coefficient to list for convenient coding.
                coefficient = list(coefficient)
                for item in coefficient:
                    assert type(item) in (int, float), \
                        'There are non number in coefficient.'
                assert len(coefficient) >= len(exponent), \
                    'coefficient should be equal or longer than exponent.'

                # main loop for append().
                for index in range(len(exponent)):
                    if exponent[index] in self:
                        return False
                    elif coefficient[index] == 0:
                        pass
                    else:
                        self[exponent[index]] = coefficient[index]
                return True

            #
            # exponent is iterable.
            # coefficient is integer.
            #
            else:
                assert len(exponent) == 1, \
                    'coefficient has too many elements than exponent'

                # main loop for append().
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
            #
            # exponent is integer.
            # coefficient is iterable.
            #
            if self._iterable(coefficient):
                coefficient = list(coefficient)
                assert len(coefficient) >= 1,\
                    f'{coefficient} is empty!'

                # main for append().
                if exponent in self:
                    return False
                else:
                    if not coefficient[0]:
                        return True
                    self[exponent] = coefficient[0]
                    return True

            #
            # exponent is integer.
            # coefficient is iteger.
            #
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
        exponent exist in data(self). If exist, sum pairing coefficient in
        already existing coefficient in data.
        If does not exist, append the (coefficient, exponent) in data. But if
        coefficient is 0 or 0.0, the (coefficient, exponent) is never appended.
        If coefficient has more elements than exponent, do not use the elements
        of coefficient after len(exponent)_index.

        :param coefficient: package of coefficient that appended in data
        :type coefficient:  int or iterable(list, tuple etc...)

        :param exponent: package of exponent that appended in data
        :type exponent:  int or iterable(list, tuple etc...)

        :returns: none
        :rtype:   none

        :precondition: elements in coefficient and exponent should be numeric.
        """
        assert type(coefficient) in (int, float)\
            or self._iterable(coefficient), \
            f'{repr(coefficient)} does not satisfy the precondition.'
        assert type(exponent) in (int, float) or self._iterable(exponent), \
            f'{repr(exponent)} does not satisfy the precondition.'

        # If exponent is iterable
        if self._iterable(exponent):

            # convert sequence to list for convenient coding.
            exponent = list(exponent)
            for item in exponent:
                assert type(item) == (int or float), \
                    'There are non number in exponent'

            #
            # exponent is iterable.
            # coefficient is iterable.
            #
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

            #
            # exponent is iterable.
            # coefficient is integer.
            #
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
            #
            # exponent is integer.
            # coefficient is iterable.
            #
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

            #
            # exponent is integer.
            # coefficient is iteger.
            #
            else:
                if not coefficient:
                    pass

                elif exponent in self:
                    self[exponent] += coefficient
                else:
                    self[exponent] = coefficient

    @staticmethod
    def _key_func_0(pair):
        """helper method for Class Poly

        If 2-tuples is inputed, for here it means (coefficient, exponent)
        is inputed, return the first element of that. This method is made to
        help Class Poly.

        :param pair: 2-tuples (coefficient, exponent)
        :type pair:  tuple

        :returns: first element in data
        :rtype:   int or float (it's up to coefficient)
        """
        assert type(pair) == tuple,\
            repr(pair) + 'is not tuple pair'

        return pair[0]

    @staticmethod
    def _key_func_1(pair):
        """helper method for Class Poly

        If 2-tuples is inputed, for here it means (coefficient, exponent)
        is inputed, return the second element of that. This method is made to
        help Class Poly.

        :param pair: 2-tuples (coefficient, exponent)
        :type pair:  tuple

        :returns: first element in data
        :rtype:   int
        """
        assert type(pair) == tuple,\
            repr(pair) + 'is not tuple pair'

        return pair[1]

    def get_expon(self, coeff1, coeff2=None):
        """Get exponent in limited range.

        If coeff2 is None, coeff1 should be integer. Then find the data which
        coeffcient is coeff1. Then return those tuples as list-of-2-tuples
        in decreasing order.
        If coeff2 in not None, then find the exponent which coefficient is in
        [coeff1, coeff2]. And then hen return those tuples as list-of-2-tuples
        in decreasing order.

        :param coeff1: if coeff2 == none:
                            specific coefficient.
                       if coeff2 != none:
                           first part of range.
        :type coeff1:  if coeff2 == none:
                            int
                       if coeff2 != none:
                            int or float

        :param coeff2: default value is None.
                       if it does not use default value, it will indicate the
                       last part of range
        :type coeff2:  (None type) or (int or float)
        """
        if coeff2 is None:
            assert type(coeff1) in (int,),\
                'As coeff2 is None, coeff1 should be integer.'

            r_list = []
            for exp, coeff in self.items():
                if coeff == coeff1:
                    r_list.append((coeff, exp))
            # Sort the list in decreasing.
            r_list.sort(key=self._key_func_1, reverse=True)
            return r_list

        else:
            assert type(coeff1) in (int, float),\
                'coeff1 do not satisfy the precondition.'
            assert type(coeff2) in (int, float),\
                'coeff2 do not satisfy the precondition.'
            r_list = []
            for exp, coeff in self.items():
                if coeff in range(coeff1, coeff2 + 1):
                    r_list.append((coeff, exp))
            # Sort the list in decreasing.
            r_list.sort(key=self._key_func_1, reverse=True)
            return r_list

    def max_expon(self):
        """Return the 2-tuple which exponent is the biggest.

        Make the new list-of-2-tuples which data is self.
        Then sort that list in decreasing based on exponent. Then return the
        first element of new list-of-2-tuples which indicates maximum exponent.

        :return: 2-tuple of maximum exponent
        :rtype:  tuple
        """
        poly_list = self.tuplelist()
        poly_list.sort(key=self._key_func_1, reverse=True)

        return poly_list[0]

    def min_expon(self):
        """Return the 2-tuple which exponent is the smallest.

        Make the new list-of-2-tuples which data is self.
        Then sort that list in increasing based on exponent. Then return the
        first element of new list-of-2-tuples which indicates minimum exponent.

        :return: 2-tuple of minimum exponent
        :rtype:  tuple
        """
        poly_list = self.tuplelist()
        poly_list.sort(key=self._key_func_1)

        return poly_list[0]

    def max_coeff(self):
        """Return the list-of-2-tuples which coefficient is the biggest.

        Make the new list-of-2-tuples which data is self.
        Then sort the list in decreasing based on coefficient.
        Then append 2-tuples in r_list from the start until coefficient is
        changed. Then sort the r_list in decreasing based on exponent.

        :return: list-of-2-tuples which coefficient is max.
        :rtype:  list
        """
        poly_list = self.tuplelist()
        poly_list.sort(key=self._key_func_0, reverse=True)

        r_list = []
        # maximum coefficient
        max_value = poly_list[0][0]
        for term in poly_list:
            if term[0] == max_value:
                r_list.append(term)
            else:
                break
        r_list.sort(key=self._key_func_1, reverse=True)
        return r_list

    def min_coeff(self):
        """Return the list-of-2-tuples which coefficient is the smallest.

        Make the new list-of-2-tuples which data is self.
        Then sort the list in increasing based on coefficient.
        Then append 2-tuples in r_list from the start until coefficient is
        changed. Then sort the r_list in decreasing based on exponent.

        :return: list-of-2-tuples which coefficient is min.
        :rtype:  list
        """
        poly_list = self.tuplelist()
        poly_list.sort(key=self._key_func_0)

        r_list = []
        # minimum coefficient
        min_value = poly_list[0][0]
        for term in poly_list:
            if term[0] == min_value:
                r_list.append(term)
            else:
                break
        r_list.sort(key=self._key_func_1, reverse=True)
        return r_list

# -- end of 2020313793.정우성.HW10.py
