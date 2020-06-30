#!/usr/bin/env python3
#
#  Copyright (c) 2020 by 민형복, All rights reserved.
#  Copyright (c) 2020 by 정우성, All rights reserved.
#
#  File       : 2020313793.정우성.HW11.py
#  Written on : Jun. 07, 2020
#
#  Student ID : 2020313793
#  Author     : 정우성  (wsung0011@naver.com)
#  Affiliation: School of Electrical Engineering
#               Sungkyunkwan University
#  py version : tested by CPython 3.8.2, 64-bit
#  Class      : Engineering Computer Programming (GEDT018-43)
#  Subject    : Lab-11, 'Operators and Setters/Getters' program
#
#  Modification History:
#     * version 1.0, by 정우성, Jun. 07, 2020
#       - 1st released on this day.
#  end of Modification History
#
"""A module with Poly class with operator methods and getters/setters.

This is a module for practicing 'Operators and Setters/Getters' of class.
One class 'Poly' are packed here. 'Poly' Class inherit the 'dict'.
With this class, you can sum or time the each polynomial.
But sadly, it is impossible for divding and subtracting with this class.
Also, it is possible to set or get the informations of Poly.
After the evaluating, the data of poly is sorted in decreasing by exponent.

Class:
    Poly : Polynomial inherited from dict.

    :example:
        p1 = Poly([(2, 6), (-7, 4), (1, 1), (9, 0)])
        p2 = Poly([(3, 5), (1, 4), (2, 0)])

        p1 + p2; Poly({6: 2, 5: 3, 4: -6, 1: 1, 0: 11})
        p1 * p2; Poly({11:6, 10:2, 9:-21, 8:-7, 6:7, 5:28, 4:-5, 1:2, 0:18}]

All elements in parameter should be numeric.
For more details, please check each methods in class Poly.
"""


class Poly(dict):
    """Polynomial inherited from dict.

    Simple class that conatains the method which handle the coefficient and
    exponent of polynomial with operator.
    You can make poly obeject with "obj = Poly(dict or list-of-2-tuples)"
    You can enter nothing in parameter cause it has default value '{}'.
    Here, list-of-2-tuples means the list of tuples with numer pair.
    :example:
        obj = Poly()
        obj = Poly({1:2, 2:3})
        obj = Poly([(1,2), (2,3)])

    :super class: dict

    :public method:
        obj.poly
            :Get the informations of polynomial in dict form.
        obj = poly(dict)
            : Set the new informations in obj.
        obj.tuplelist
            : Get polynomial as a list of tuples.
        obj = tuplelist(iterable)
            : Set the new informaions in obj

    :public operators:
        + operator
            : Sum the two polynomials
        * operator
            : Times the two polynomials
    """

    def __init__(self, d={}):
        """Initializer of Poly class.

        This class used dict's intializer. And do not override the __init_.
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

    @staticmethod
    def _iterable(obj):
        """Helper method to check if given object is iterable.

        This method checks if given object ''obj'' is iterable or not.
        FYI, you may use isinstance(obj, Iterable) defined at collections.abc.

        :param obj: We check if this ''obj'' is iterable or not.
        :type obj: any

        :returns: True if ''obj'' is iterable, False otherwise.
        :rtype: bool
        """
        try:
            iter(obj)
        except TypeError:
            return False
        else:
            return True

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

    def __str__(self):
        """str() method.

        Return the form of data that you entered when construct the class.
        Use print() to use these method.

        :returns: form of self
        :rtype:   str
        """
        return super().__repr__()

    def __repr__(self):
        """repr() method.

        Return the information of data when construct the class.
        Use repr() to use these method.

        :returns: form that can make class
        :rtype:  str
        """
        return 'Poly(' + super().__repr__() + ')'

    @property
    def poly(self):
        """return: polynomial as a dict

        get a polynomial in dictionary form.

        :returns: form of dict
        :rtpye:   dict
        """
        return dict(self)

    @poly.setter
    def poly(self, value):
        '''Setter for self with new value which is dictionary.

        Delete the self's information. Then, re__init__ the self with
        given value.

        :param value: new information for setting
        :type value:  dict

        :returns: none
        :rtype:   none

        :precondition:
            all elements in value should be int or float
        '''
        assert type(value) == dict,\
            repr(value) + 'does not satisfy the preconditoin'
        for exp, coeff in tuple(self.items()):
            assert type(coeff) in (int, float),\
                repr(coeff) + 'does not satisfy the precondition.'
            assert type(exp) in (int,),\
                repr(exp) + 'does not satisfy the precondition.'

        for exp in tuple(self.keys()):
            del self[exp]
        self.__init__(value)

    @property
    def tuplelist(self):
        """Get polynomial as a list of (coefficient, exponent) tuples.

        Return the polynomial in a list-of-2-tuples form

        :returns: list-of-2-tuples of terms
        :rtype:   list
        """
        r_list = []
        for exp, coeff in (dict(self)).items():
            r_list.append((coeff, exp))
        r_list.sort(key=self._key_func_1, reverse=True)
        return r_list

    @tuplelist.setter
    def tuplelist(self, value):
        '''Setter for self with new value which is 2=tuple-list

        Delete the self's information. Then, re__init__ the self with
        given value.

        :param value: new information for setting
        :type value:  interable

        :returns: none
        :rtype:   none

        :precondition:
            all elements in value should be int or float
        '''
        assert self._iterable(value) is True,\
            repr(value) + 'does not satisfy the precondition.'
        for coeff, exp in value:
            assert type(coeff) in (int, float),\
                repr(coeff) + 'does not satisfy the precondition.'
            assert type(exp) in (int,),\
                repr(exp) + 'does not satisfy the precondition.'

        for exp in tuple(self.keys()):
            del self[exp]
        self.__init__(value)

    def __add__(self, other):
        """Support + operator on two polinomials.

        Poly class support the + operator between two polinomials.
        The plus rule follows the common polynomial math.

        :param other: same Poly class which will be added
        :type other:  Poly

        :returns: final data of sums with sorting.
        :rtype:   Poly
        """

        assert type(other) in (Poly,),\
            repr(other) + 'is not Poly class'

        # result_dict for arranging the data.
        result_dict = {}
        for exp, coeff in self.items():
            result_dict[exp] = coeff
        for exp, coeff in other.items():
            if exp in result_dict:
                result_dict[exp] += other[exp]
                if result_dict[exp] == 0:
                    del result_dict[exp]
            else:
                result_dict[exp] = other[exp]

        # result_list for sorting the results.
        result_list = []
        for exp, coeff in result_dict.items():
            result_list.append((coeff, exp))
        result_list.sort(key=self._key_func_1, reverse=True)

        r_val = {}
        for coeff, exp in result_list:
            r_val[exp] = coeff

        return Poly(r_val)

    def __mul__(self, other):
        """Support * operator on two polinomials.

        Poly class support the * operator between two polinomials.
        The times rule follows the common polynomial math.

        :param other: same Poly class which will be timed
        :type other:  Poly

        :returns: final data of sums with sorting.
        :rtype:   Poly
        """

        assert type(other) in (Poly,),\
            repr(other) + 'is not Poly class'

        # result_dict for arranging the data.
        result_dict = {}
        self_key = tuple(self.keys())
        other_key = tuple(other.keys())
        for val1 in self_key:
            for val2 in other_key:
                if val1+val2 in result_dict:
                    result_dict[val1+val2] += self[val1]*other[val2]
                else:
                    result_dict[val1+val2] = self[val1]*other[val2]

        # result_list for sorting the results.
        result_list = []
        for exp, coeff in result_dict.items():
            result_list.append((coeff, exp))
        result_list.sort(key=self._key_func_1, reverse=True)

        r_val = {}
        for coeff, exp in result_list:
            r_val[exp] = coeff

        return Poly(r_val)

# -- end of 2020313793.정우성.HW11.py
