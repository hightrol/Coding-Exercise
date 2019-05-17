# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:29:34 2018

@author: haimingwd
"""

## for all-low-cap strings count frequency, return tuple
def maketuple(str0):
    lst = [0 for i in range(26)]
    for char in str0:
        lst[ord(char) - ord('a')] += 1
    return tuple(lst)

## group a list of all-low-cap strings based on anagrams
def groupAnagrams(strs):
    dct = {}
    for i in range(len(strs)):
        t1 = maketuple(strs[i])
        dct[t1] = dct.get(t1, []) + [i]
    lst = []
    for val in dct.values():
        lst.append([strs[k] for k in val])
    return lst

