# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:29:30 2018

@author: haimingwd
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
def commonAncestor(root, node1, node2):
    x = None
    def dfs(root0):
        ## 注意如何解决变量作用域的问题
        ## 或者可以像leetcode一样通过定义solution类, 将x变为attribute解决
        global x
        if not root0:
            return False, False
        else:
            l1, l2 = dfs(root0.left)
            r1, r2 = dfs(root0.right)
            a = True if root0 == node1 or l1 or r1 else False
            b = True if root0 == node2 or l2 or r2 else False
            if a and b:
                if not x:
                    x = root0
            else:
                return a,b
    dfs(root)
    if x:
        return x
    else:
        print("No Common Ancestor")
        return None
    

                
    
    