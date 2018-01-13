# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:19:03 2018

@author: haimingwd
"""

def hammingDist(x, y):
    n = x^y
    dist = 0
    ## the while loop counts how many '1' do we have for n
    while n:
        dist += 1
        n &= n-1
    return dist
    