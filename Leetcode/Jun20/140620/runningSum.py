#!/usr/bin/python3


""" 
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        rList = list()
        
        for i in range(len(nums)):
            n = nums[i] + total
            rList.append(n)
            total += nums[i]
            
        return rList
