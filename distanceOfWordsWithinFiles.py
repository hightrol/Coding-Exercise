# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:59:03 2018

@author: haimingwd
"""

## distance of words within files

class Dist:
    
    def __init__(self, text = ''):
        textFile = text.split()
        self.wordLoc = {}
        n = len(textFile)
        for i in range(n):
            word = textFile[i]
            self.wordLoc[word] = self.wordLoc.get(word, []) + [i]
        self.total = n
        
    def add(self, text):
        textFile = text.split()
        n = len(textFile)
        for i in range(n):
            word = textFile[i]
            self.wordLoc[word] = self.wordLoc.get(word, []) + [self.total+i]
        self.total += n
        
    def dist(self, word1, word2):
        x = self.wordLoc.get(word1, [])
        y = self.wordLoc.get(word2, [])
        if not x:
            raise Exception("Not find {}".format(word1))
        if not y:
            raise Exception("Not find {}".format(word2))
        n1, n2 = len(x), len(y)
        min_dist = self.total
        i, j = 0, 0
        while i < n1 and j < n2:
            min_dist = min(min_dist, abs(x[i] - y[j]))
            if min_dist == 1:
                break
            if x[i] <= y[j]:
                i += 1
            else:
                j += 1 
        return min_dist
    
d = Dist()
d.add("a c a c b a d c")
d.dist('a', 'b')
d.dist('a', 'd')
d.dist('b', 'd')
            
            
            
            
            
            
            
            
            
            