#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 29, 2020 13:45:47 AEDT
  @file        : mostComp

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(msg)s")

class Solution:
    def mostCompetitive(self, nums, k):
        # if k is same length as input, then we don't need to do anything
        if k == len(nums): return nums 

        """
        Algo:

        We use a stack to keep track of recent minimum elements

        We do this because order needs to be preserved first and foremost,
        but also because we want to place smallest element we can into
        our output stack while making sure that there will be k elements
        in our stack at the end.

        With this in mind, as long as the size of our stack + remaining elements > k,
        we can pop our stack and replace it with a smaller element

        TC: O(N) - we do one pass of nums
        SC: O(K) - we create a stack with at most k elements

        """

        # stack to keep track of sequence
        s = list()

        for i,v in enumerate(nums):
            
            # While we have a stack, and there's a smaller number than the top of it,
            # we can pop the stack provided there's enough elements left in the original
            # list to ensure we end up with k elements at the end of the day
            while s and s[-1] > v and len(s) + len(nums) - i > k:
                s.pop()

            # If the stack already has k elements and the next v is greater
            # than the top, we shouldn't add it
            # Otherwise we end up with a stack that will be larger than k
            if len(s) < k:
                s.append(v)

        return s




