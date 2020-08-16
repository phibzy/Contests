#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 16, 2020 12:52:53 AEST
  @file        : q1

Given an array, return true if there are 3 consecutive odd numbers in it.

Return false otherwise.


"""




class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for i in arr:
            if i % 2 == 1:
                odd += 1
                if odd == 3: return True
            else:
                odd = 0
                
        return False
