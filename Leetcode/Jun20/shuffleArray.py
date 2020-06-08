#!/usr/bin/python3

class Solution:
    def shuffle(self, nums, n):
        rList = list()
        
        i = 0
        while i < n:
            rList.append(nums[i])
            rList.append(nums[i + n])
            i += 1
            
        return rList
