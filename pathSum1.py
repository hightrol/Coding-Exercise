# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:08:14 2018

@author: haimingwd
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
## print out paths from root to leaves that has a sum of target
        
def pathSum1(root, target):
    
    def dfs(node, history, sum0):
        if node:
            if (not node.left) and (not node.right):
                if sum0 + node.val == target:
                    print(history+[node])
            else:
                if node.left:
                    dfs(node.left, history+[node], sum0+node.val)
                if node.right:
                    dfs(node.right, history+[node], sum0+node.val)
    
    dfs(root, [], 0)
    
    
        