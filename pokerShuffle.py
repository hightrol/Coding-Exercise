# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:11:28 2018

@author: haimingwd
"""
import numpy as np

## Shuffle by sort
def pokerShuffle1(lst):
    n = len(lst)
    rand_arr = np.random.rand(n)
    ix = sorted([i for i in range(n)], key = lambda x:rand_arr[x])
    return [lst[i] for i in ix]


## Knuth Shuffle
def pokerShuffle2(lst):
    n = len(lst)
    for i in range(n):
        randx = np.random.randint(i,n)
        lst[i], lst[randx] = lst[randx], lst[i]
    return lst