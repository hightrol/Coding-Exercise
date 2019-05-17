# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:37:59 2018

@author: haimingwd
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## Morris Traversal, in-order traversal with constant space complexity
def MorrisTraversal(root):
    result = []
    p = root
    while p:
        if not p.left:
            result.append(p.val)
            p = p.right
        else:
            prev = p.left
            while prev.right and prev.right != p:
                prev = prev.right
            if not prev.right:
                prev.right = p
                p = p.left
            else:
                prev.right = None
                result.append(p.val)
                p = p.right

