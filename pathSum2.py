# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:48:16 2018

@author: haimingwd
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## print out paths from any nodes to another (child) nodes that has a sum of target

def pathSum2(root, target):
    
    def dfs(root0, history):
        if root0:
            n = len(history)
            ## print out paths that end with root0
            sum0 = root0.val
            xx = [root0.val]
            if sum0 == target:
                print(xx)
            for i in range(n):
                sum0 += history[n-1-i]
                xx += [history[n-1-i]]
                if sum0 == target:
                    print(xx[::-1])
            if root.left:
                dfs(root.left, history + [root0.val])
            if root.right:
                dfs(root.right, history + [root0.val])
        else:
            pass
        
    dfs(root, [])