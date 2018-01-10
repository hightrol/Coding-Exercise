# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:30:16 2018

@author: haimingwd
"""

## implement a queue using two stacks

class Queue:
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def push(self, x):
        self.in_stack.append(x)
        
    def peak(self):
        if self.out_stack:
            return self.out_stack[-1]
        else:
            if not self.in_stack:
                raise Exception("No elements")
            while self.in_stack: 
                x = self.in_stack.pop()
                self.out_stack.append(x)
            
    def pop(self):
        if self.out_stack:
            self.out_stack.pop()
        else:
            if not self.in_stack:
                raise Exception("No elements")
            while self.in_stack: 
                x = self.in_stack.pop()
                self.out_stack.append(x)
            self.out_stack.pop()
    
            
                