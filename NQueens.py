# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:09:47 2018

@author: haimingwd
"""

def solveNQueens(n):
    
    result = []
    
    def dfs(lst, xydiff, xysum):
        i = len(lst)
        if i == n:
            result.append(lst)
            return
        for j in range(n):
            if (j not in lst) and (i+j not in xysum) and (i-j not in xydiff):
                dfs(lst+[j], xydiff + [i-j], xysum + [i+j])
    
    def convert1(num):
        str0 = '.'*(num) + 'Q' + '.'*(n-num-1)
        return str0
    
    def convert2(lst):
        return list(map(convert1, lst))
    
    dfs([], [], [])
    return list(map(convert2, result))


solveNQueens(6)
