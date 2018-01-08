# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:24:02 2018

@author: haimingwd
"""


## minesweeper
## modify game board in place
def updateBoard(board, click):
    
    m, n = len(board), len(board[0])
    
    def bd(i, j):
        if i < 0 or i >= m or j < 0 or j >= n: 
            return None
        else:
            return board[i][j]
    
    def minaround(i, j):
        return sum([bd(i+x, j+y) == 'M' for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]])
    
    def dfs(i,j):
        x = bd(i,j)
        if not x:
            pass
        elif x == 'M':
            board[i][j] = 'X'
        elif (x < '9' and x >= '1') or x == 'B':
            pass
        elif minaround(i, j) > 0:
            board[i][j] = str(minaround(i,j))
        else:
            board[i][j] = 'B'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                dfs(i+x, j+y)
    
    dfs(click[0], click[1])
