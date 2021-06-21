#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jun 21 08:44:22 2021

@author: Hankui Peng

"""

nums1 = [1,2,2,1] 
nums2 = [2,2]



#%%
class Solution:
    
    def intersect(self, nums1, nums2):
        
        dict_nums1 = {}
        for v in nums1:
            if v not in dict_nums1:
                dict_nums1[v] = 1
            else:
                dict_nums1[v] += 1
        
        dict_nums2 = {}
        for v in nums2:
            if v not in dict_nums2:
                dict_nums2[v] = 1
            else:
                dict_nums2[v] += 1
                
        ans = []
        if len(dict_nums1) < len(dict_nums2):
            for v in dict_nums1:
                if v in dict_nums2:
                    count = min(dict_nums2[v], dict_nums1[v])
                    ans.extend([v]*count) 
                else:
                    pass
        else:
            for v in dict_nums2:
                if v in dict_nums1:
                    count = min(dict_nums2[v], dict_nums1[v])
                    ans.extend([v]*count) 
                else:
                    pass   
        
        return ans 