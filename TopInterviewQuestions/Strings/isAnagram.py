#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 28 09:31:00 2021

@author: Hankui Peng

"""

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/
from typing import List 


s = "anagram" 
t = "nagaram"

s = "rat" 
t = "car"

s = "a"
t = "ab"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = {}
        dict_t = {}
        
        ans = True 
        
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
        for i in range(len(t)):
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        
        if len(dict_s) == len(dict_t):
            for v in dict_s:
                if (v in dict_t) and (dict_s[v] == dict_t[v]):
                    pass 
                else:
                    ans = False
                    break 
        else:
            ans = False 
        return ans 
    
    def isAnagram_solution(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


#%%
method = Solution()
method.isAnagram(s, t)
method.isAnagram_solution(s, t)


#%%
dict_s = {}
dict_t = {}

ans = True 

for i in range(len(s)):
    if s[i] in dict_s:
        dict_s[s[i]] += 1
    else:
        dict_s[s[i]] = 1
    
    if t[i] in dict_t:
        dict_t[t[i]] += 1
    else:
        dict_t[t[i]] = 1

if len(dict_s) == len(dict_t):
    for v in dict_s:
        if (v in dict_t) and (dict_s[v] == dict_t[v]):
            pass 
        else:
            ans = False
            break 
else:
    ans = False 