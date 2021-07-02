#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Jul  2 09:14:16 2021

@author: Hankui Peng

"""

### Solution: https://leetcode.com/problems/rotate-image/solution/


matrix = [[1,2,3],[4,5,6],[7,8,9]]


#%%
tmp = matrix[0][0]
matrix[0][0] = matrix[0][-1]
