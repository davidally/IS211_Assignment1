#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):

    total = 0

    for x in numbers:
        if x % divide == 0:
            total += 1
    return total

def testListDivide():

    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], divide=1)
    except:
        raise ListDivideException

testListDivide()
