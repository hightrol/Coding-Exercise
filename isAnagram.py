# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:28:14 2018

@author: haimingwd
"""

## small cap strings:s and t
## otherwise use dict
def isAnagram(self, s, t):
    
    if len(s) != len(t):
        return False
    count_s = [0 for i in range(26)]
    count_t = [0 for i in range(26)]
    for char in s:
        count_s[ord(char) - ord('a')] += 1
    for char in t:
        count_t[ord(char) - ord('a')] += 1
    for i in range(26):
        if count_s[i] != count_t[i]:
            return False
    return True