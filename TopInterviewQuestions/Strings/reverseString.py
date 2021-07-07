#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul  7 09:03:41 2021

@author: Hankui Peng

"""

s = ["h","e","l","l","o"]
s = ['b', 'i', 'k', 'e']


from typing import List 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n//2):
            tmp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = tmp
        
        return s 


#%%
n = len(s)

for i in range(n//2):
    tmp = s[i]
    s[i] = s[-(i+1)]
    s[-(i+1)] = tmp


#%%
solution = Solution()
solution.reverseString(s)
