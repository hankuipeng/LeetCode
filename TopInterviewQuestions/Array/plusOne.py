#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Jun 25 14:08:15 2021

@author: hankui
"""

digits = [4,3,2,1]
digits = [9,9]
digits = [8,9,9,9]


#%% 
import numpy as np
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num_str = ''
        for v in digits:
            num_str += str(v)
        
        num_output = int(num_str) + 1
        
        return [int(v) for v in str(num_output)]


#%%
method = Solution()
method.plusOne(digits)
