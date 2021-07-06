#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Jul  2 09:14:16 2021

@author: Hankui Peng

"""

### Solution: https://leetcode.com/problems/rotate-image/solution/

matrix = [[1,2],[3,4]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


#%%
tmp = matrix[0][0]
matrix[0][0] = matrix[-1][0]
matrix[-1][0] = matrix[-1][-1] # bottom left 
matrix[-1][-1] = matrix[0][-1] # bottom right 
matrix[0][-1] = tmp # top right


#%%
n = len(matrix)
    
for i in range((n//2) + (n%2)):
    for j in range(n//2):
    # =============================================================================
    #     import pdb
    #     pdb.set_trace()
    # =============================================================================
        tmp = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
        matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
        matrix[j][n - 1 - i] = matrix[i][j]
        matrix[i][j] = tmp


#%%
