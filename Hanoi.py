# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:58:59 2018

@author: haimingwd
"""

## Hanoi tower game

class Hanoi:
    
    def __init__(self, n):
        self.list_stack = [[n-i for i in range(n)], [], []]
        self.steps = 0
    
    def show(self):
        print("Show 3 stacks")
        print("Now step: " + str(self.steps))
        for i in range(3):
            print(self.list_stack[i])
        print("End of show\n")
        
    def move(self, start, end, disks):
        if len(self.list_stack[start]) < disks:
            raise Exception("don't have so many disks")
        if disks == 1:
            x = self.list_stack[start].pop()
            self.list_stack[end].append(x)
            self.steps += 1
        else:
            self.move(start, 3-start-end, disks-1)
            self.move(start, end, 1)
            self.move(3-start-end, end, disks-1)
        self.show()

h = Hanoi(4)        
h.show()
h.move(0, 2, 3)
            
        
        
            
    