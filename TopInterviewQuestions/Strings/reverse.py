#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul  7 09:19:17 2021

@author: Hankui Peng

"""

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        n = len(x_str) 
        x_rev = 0
        
        if x < 0:
            x_rev = -int(x_str[::-1][:-1])
            if (x_rev < -2**31):
            #if n > len(str(-2**31)):
                x_rev = 0
        
        if x > 0:
            x_rev = int(x_str[::-1])
            if (x_rev > (2**31 - 1)):
            #if n > len(str(2**31-1)):
                x_rev = 0
        
        return x_rev 


#%%
x = 123
x = -123
x = 1534236469
x = -2147483648


#%%
x_str = str(x)

if x < 0:
    x_rev = -int(x_str[::-1][:-1])
    if (-x_rev < -2**31):
        x_rev = 0

if x > 0:
    x_rev = int(x_str[::-1])
    if (x_rev > (2**31 - 1)):
        x_rev = 0


#%%
solution = Solution()
solution.reverse(x)
