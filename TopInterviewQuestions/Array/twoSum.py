#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 30 10:16:41 2021

@author: Hankui Peng

"""


#%%
nums = [11,2,7,15]
target = 9

nums = [-1,-2,-3,-4,-5]
target = -8


#%% draft
ans = []
for i, v in enumerate(nums):
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    for j, v2 in enumerate(nums[(i+1):]):
        if v + v2 == target:
            ans = [i,j+i+1]
            break 
    if (len(ans) > 0):
        break 


#%%
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        for i, v in enumerate(nums):
            for j, v2 in enumerate(nums[(i+1):]):
                if v + v2 == target:
                    ans = [i,j+i+1]
                    break 
            if (len(ans) > 0):
                break 
        
        return ans 