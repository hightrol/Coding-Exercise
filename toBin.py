# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:34:11 2018

@author: haimingwd
"""

def divide(lst):        
    i, b = 0, 0
    result = []
    for i in range(len(lst)):
        a, b = (10*b + lst[i])//2, (10*b + lst[i])%2
        result.append(a)
    return result if result[0] != 0 else result[1:], b
        

def toBin(lst):
    if len(lst) == 1:
        return list(map(int, bin(lst[0])[2:]))
    a, b = divide(lst)
    return toBin(a) + [b]