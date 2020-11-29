#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 29, 2020 13:36:33 AEDT
  @file        : maximumWealth

"""

class Solution:
    def maximumWealth(self, accounts) -> int:
        # TL;DR it will be the largest sum of the elements

        maxSum = 0

        for i in accounts:
            maxSum = max(sum(i), maxSum)

        return maxSum
