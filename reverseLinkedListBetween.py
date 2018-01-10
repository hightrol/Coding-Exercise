# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:08:57 2018

@author: haimingwd
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## Reverse linked list between m-th and n-th nodes(include both)

def reverseBetween(head, m, n):
    i = 0
    dummy = ListNode(0)
    dummy.next = head
    p1 = dummy
    while i < m-1:
        p1 = p1.next
        i += 1
    p2 = p4 = p1.next
    p3 = p2.next
    while i < n-1:
        p3.next, p2, p3 = p2, p3, p3.next
        i += 1
    p1.next = p2
    p4.next = p3
    return dummy.next