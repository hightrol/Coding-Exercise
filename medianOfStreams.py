# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:00:20 2018

@author: haimingwd
"""

### find median from number streams

import heapq as hq
## 小堆

class Streams:
    
    def __init__(self):
        ## negative of smaller numbers, stored in min_heap
        self.sHeap = []
        ## larger numbers, stored in min_heap
        self.lHeap = []
        
    def add(self, x):
        if not self.sHeap:
            hq.heappush(self.sHeap, -x)
        elif not self.lHeap:
            hq.heappush(self.lHeap, x)
        elif len(self.sHeap) == len(self.lHeap):
            if x <= self.lHeap[0]:
                hq.heappush(self.sHeap, -x)
            else:
                temp = hq.heappop(self.lHeap)
                hq.heappush(self.sHeap, -temp)
                hq.heappush(self.lHeap, x)
        else:
            if x >= -self.sHeap[0]:
                hq.heappush(self.lHeap, x)
            else:
                temp = hq.heappop(self.sHeap)
                hq.heappush(self.lHeap, -temp)
                hq.heappush(self.sHeap, x)
        
    def median(self):
        if len(self.sHeap) > len(self.lHeap):
            return -self.sHeap[0]
        elif self.sHeap:
            return (-self.sHeap[0] + self.lHeap[0])/2
        else:
            raise Exception("Empty stream flow")
            
    def showAll(self):
        lst = [-x for x in self.sHeap] + self.lHeap
        print(lst)
            
s = Streams()
s.add(1)
s.add(3)
s.median()
s.add(2)
s.median()
s.add(2.5)
s.median()
s.add(1.5)
s.median()
s.add(12)
s.median()
s.showAll()

        