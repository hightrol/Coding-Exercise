# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:33:40 2018

@author: haimingwd
"""

def Josephus(lst, k):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) >= k:
        return Josephus(lst[k:] + lst[:(k-1)], k)
    else:
        m = k % len(lst)
        return Josephus(lst[m:] + lst[:(m-1)], k)
        