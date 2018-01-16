# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 15:32:16 2018

@author: haimingwd
"""

def longestChain(lst):
    lst.sort()
    seq_dict = {}
    n = len(lst)
    for i in range(n):
        if i == 0:
            seq_dict[i] = [i]
        else:
            max_len_ix = 0
            for j in seq_dict:
                if lst[j][1] <= lst[i][1]:
                    if len(seq_dict[j]) > len(seq_dict[max_len_ix]):
                        max_len_ix = j
            max_len_seq = seq_dict[max_len_ix] + [i]
            seq_dict[i] = max_len_seq
        print(seq_dict)
    print(seq_dict)
    u = max([i for i in range(n)], key = lambda x:len(seq_dict[x]))
    return seq_dict[u]

longestChain(x)
