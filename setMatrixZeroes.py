# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:35:25 2018

@author: haimingwd
"""

## For an M*N matrix, set row or column to be 0 if an element is 0
## O(1) extra memory
def setZeroes(mtx):

    if not mtx:
        pass
    
    m, n = len(mtx), len(mtx[0])
    ## whether first column contains zero
    col = 0 if any([mtx[i][0] == 0 for i in range(m)]) else 1
    ## whether first row contains zero
    row = 0 if any([mtx[0][j] == 0 for j in range(n)]) else 1
    for i in range(1, m):
        for j in range(1, n):
            if mtx[i][j] == 0:
                mtx[i][0] = 0
                mtx[0][j] = 0
                
    print(row, col)
    print(mtx)
    
    for i in range(m-1, 0, -1):
        for j in range(n-1, 0, -1):
            mtx[i][j] *= 1 if mtx[i][0] * mtx[0][j] else 0
    if row == 0:
        for j in range(n):
            mtx[0][j] = 0
    if col == 0:
        for i in range(m):
            mtx[i][0] = 0
        
        