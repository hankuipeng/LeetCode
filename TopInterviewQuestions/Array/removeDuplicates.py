#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 16 14:28:20 2021

@author: Hankui Peng

"""

nums = [2,2,3,3,4,4]


#%% My attempt
class Solution:
    def removeDuplicates(self, nums):
        unique_vals = {}
        for i,v in enumerate(nums):
            if v not in unique_vals:
                unique_vals[v] = 1
        return [v for v in unique_vals]


#%% Solution
class Solution:
    def removeDuplicates(self, nums):
        len_ = 1
        
        if len(nums)==0:
            return 0
        
        for i in range(1, len(nums)):
            
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_

method = Solution()
method.removeDuplicates(nums)
