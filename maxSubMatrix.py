# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:01:33 2018

@author: haimingwd
"""

## Kadane's algo for 2D array

def maxSubArray(arr):
    n = len(arr)
    cumSum, minCumSum, maxSum = 0, 0, 0
    for i in range(n):
        cumSum = cumSum + arr[i]
        minCumSum = min(minCumSum, cumSum)
        maxSum = max(maxSum, cumSum - minCumSum)
    return maxSum

def maxSubMatrix(mtx):
    m, n = len(mtx), len(mtx[0])
    ## sumRow[i][j] is the sum of the i-th row from 0 to j-1
    sumRow = [[0]*(n+1) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            sumRow[i][j+1] = sumRow[i][j] + mtx[i][j]
    ## fixed left and right column of matrix, find the maxSum
    ## then compare all maxSum and get maxSubMatrix
    maxSum = 0
    for c1 in range(n):
        for c2 in range(c1, n):
            ## sumRow1[i] is the sum of the i-th row from c1 to c2
            sumRow1 = [sumRow[i][c2+1] - sumRow[i][c1] for i in range(m)]
            maxSum = max(maxSum, maxSubArray(sumRow1))
    return maxSum


maxSubArray([1,-2,3,-2,1.5,3])

maxSubMatrix([[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]])
            
    
    