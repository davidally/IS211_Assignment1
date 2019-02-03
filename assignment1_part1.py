#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 - Part 1"""


class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):
    """This function checks if an array has divisble numbers.
    
    This function will take an array and number. The array will
    be checked against the number to see if any of it's indexes 
    are divisible by the number. It then will tell you the total 
    amount of items that are divisible by the number. 
    
    Args:
        numbers (array): An array of numbers.
        divide (int, optional): Defaults to 2. The amount to divide by. 
        each item in the array by.
    
    Returns:
        int: The total amount of items divisible by divide.
    """

    total = 0

    for x in numbers:
        if x % divide == 0:
            total += 1
    return total

def testListDivide():
    """This function will test all cases.
    
    This function will test each case and raise and
    exception if there is anything wrong.
    
    Raises:
        ListDivideException: A generic exception.
    """

    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], divide=1)
    except:
        raise ListDivideException

testListDivide()
