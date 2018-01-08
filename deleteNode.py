# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:31:16 2018

@author: haimingwd
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
## delete node in a linked list, given only the node in that list
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
    