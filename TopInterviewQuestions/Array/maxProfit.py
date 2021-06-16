#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 16 15:04:38 2021

@author: Hankui Peng

"""

prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(self, prices) -> int:
        profits = 0
        
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profits += prices[i+1] - prices[i]
        
        return profits


method = Solution()        
method.maxProfit(prices)
