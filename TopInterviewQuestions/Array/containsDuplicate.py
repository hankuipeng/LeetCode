#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jun 19 11:31:30 2021

@author: hankui
"""

nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1, 2, 3, 4]

class Solution:
    def containsDuplicate(self, nums):
        
        ans = False
        distinct = {}
        
        for i, v in enumerate(nums):
            
            if v not in distinct:
                distinct[v] = 1
            else:
                ans = True
                break 
        return ans 

method = Solution()
method.containsDuplicate(nums)