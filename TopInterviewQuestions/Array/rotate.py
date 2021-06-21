#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jun 19 11:05:16 2021

@author: hankui
"""

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

nums = [3,99,-1,-100]
k = 2

nums = [1, 2]
k = 0


class Solution:
    def rotate(self, nums, k):
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if (n == 1) | (k == 0):
            return nums
        else:
        
            for i in range(k):
                
                nums.insert(0, nums[-(i+1)])
            
            del nums[-k:]
        
        return nums


method = Solution()
method.rotate(nums, k)

