# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:08:40 2018

@author: haimingwd
"""

## if str2 is in str1
def isSubString(str1, str2):
    n1, n2 = len(str1), len(str2)
    for j in range(n1-n2+1):
        if str1[j:(j+n2)] == str2:
            return True
    return False

## if str1 is an rotation of str2
def rotate(str1, str2):
    if len(str1) != len(str2):
        return False
    str3 = str1 + str1
    return isSubString(str3, str2)

rotate('aa','aa')
rotate('abcc','bcca')
rotate('abcc','ccba')


    
    