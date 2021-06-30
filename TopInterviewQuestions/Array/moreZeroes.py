#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 30 10:04:34 2021

@author: Hankui Peng

"""


#%%
from typing import List


#%%
nums = [0,0,1]


#%%
n = len(nums)
inds = []

for i,v in enumerate(nums[:n]):
    if v == 0:
        nums.append(0)
        inds.append(i)

i = 0
ind = 0
while ind < n:
    if nums[i] == 0:
        del nums[i]
    else:
        i += 1
    ind += 1


#%%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        inds = []
        
        for i,v in enumerate(nums[:n]):
            if v == 0:
                nums.append(0)
                inds.append(i)
        
        i = 0
        ind = 0
        while ind < n:
            if nums[i] == 0:
                del nums[i]
            else:
                i += 1
            ind += 1
        
        return nums 