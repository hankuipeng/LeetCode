#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Jul  1 12:09:55 2021

@author: Hankui Peng

"""

#%%
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board


#%% draft
import numpy as np

def checkValid(entries):
    
    ans = 1 # default to valid 
    num_dict = {}
    cands = [str(v) for v in range(1, 10)]
    
    for v in entries:
        if (v in cands) and (v not in num_dict):
            num_dict[v] = 1
        elif (v == "."):
            pass 
        else:
            ans = 0
            break 
    return ans 
            
    
ans = 1

## check each row 
for r in range(len(board)):
    row = board[r]
    if checkValid(row) == 0:
        ans = 0
        break

## check each column 
if ans != 0:
    for c in range(len(board[0])):
        column = [board[r][c] for r in range(len(board))]
        if checkValid(column) == 0:
            ans = 0
            break 

## check each box 
ind_pairs = [(0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)]

if ans != 0:
    for ind_pair in ind_pairs:
        i, j = ind_pair 
        entry = [board[i][j], board[i][j+1], board[i][j+2], board[i+1][j], board[i+1][j+1], board[i+1][j+2], board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
        if checkValid(entry) == 0:
            ans = 0
            break 
        

#%%
from typing import List 
import numpy as np

class Solution:

    def checkValid(self, entries):
        
        ans = 1 # default to valid 
        num_dict = {}
        cands = [str(v) for v in range(1, 10)]
        
        for v in entries:
            if (v in cands) and (v not in num_dict):
                num_dict[v] = 1
            elif (v == "."):
                pass 
            else:
                ans = 0
                break 
        return ans 

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ans = 1

        ## check each row 
        for r in range(len(board)):
            row = board[r]
            if self.checkValid(row) == 0:
                ans = 0
                break
        
        ## check each column 
        if ans != 0:
            for c in range(len(board[0])):
                column = [board[r][c] for r in range(len(board))]
                if self.checkValid(column) == 0:
                    ans = 0
                    break 
        
        ## check each box 
        ind_pairs = [(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]
        
        if ans != 0:
            for ind_pair in ind_pairs:
                i, j = ind_pair 
                entry = [board[i][j], board[i][j+1], board[i][j+2], board[i+1][j], board[i+1][j+1], board[i+1][j+2], board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                if self.checkValid(entry) == 0:
                    ans = 0
                    break 
        
        return ans 

solution = Solution()
solution.isValidSudoku(board)
