#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 28 09:21:49 2021

@author: Hankui Peng

"""

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/
from typing import List


#%%
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        ans = -1
        
        charDict = {}
        locDict = {} # dictionary to store the locations 
        for i in range(len(s)):
            if s[i] in charDict:
                charDict[s[i]] += 1
                locDict[s[i]].append(i)
            else:
                charDict[s[i]] = 1
                locDict[s[i]] = [i]
        
        
        for v in charDict:
            if charDict[v] == 1:
                ans = locDict[v][0]
                break 
        
        return ans 


s = "leetcode"
s = "aabb"

method = Solution()
method.firstUniqChar(s)


#%% Draft 
charDict = {}
locDict = {} # dictionary to store the locations 
for i in range(len(s)):
    if s[i] in charDict:
        charDict[s[i]] += 1
        locDict[s[i]].append(i)
    else:
        charDict[s[i]] = 1
        locDict[s[i]] = [i]


for v in charDict:
    if charDict[v] == 1:
        ans = locDict[v][0]
        break 