#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jun 21 08:23:31 2021

@author: Hankui Peng

"""

nums = [4,1,2,1,2]
nums = [2,2,1]
nums = [1]
nums = [1, 0, 1]


#%% Attempt 1
class Solution:
    def singleNumber(self, nums) -> int:
        
        unique_cand = nums[0]
        unique_num = nums[0]
        
        for v in nums[1:]:
            if v == unique_num:
                unique_num = []
            elif unique_num == []:
                unique_num = v
            else:
                unique_cand = v 
        if unique_num == []:
            unique_num = unique_cand 
        return unique_num 

method = Solution()
method.singleNumber(nums)


#%%
class Solution:
    def singleNumber(self, nums) -> int:
        
        val_dict = {}
        
        for v in nums:
            if v not in val_dict:
                val_dict[v] = 1
            else:
                val_dict[v] += 1
        
        for v in val_dict:
            if val_dict[v] == 1:
                ans = v
            else:
                pass
        return ans 