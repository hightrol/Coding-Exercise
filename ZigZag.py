# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:33:24 2018

@author: haimingwd
"""

## ZigZag LeetCode 6
def ZigZag(s, nRows):
    
    n = len(s)
    if nRows == 1 or nRows >= n:
        return s
    result = ['']*nRows
    ix = i = 0
    while ix < n:
        result[i] += s[ix]
        if i == 0:
            sign = 1
        if i == nRows-1:
            sign = -1
        i += sign*1
        ix += 1
    return ''.join(result)

ZigZag('PAYPALISHIRING',3)