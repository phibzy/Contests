#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 23, 2020 13:07:14 AEST
  @file        : q2

"""

class Solution:
    def maxCoins(self, piles):
        # if only 2 left case (instead of 3)

        start = 0
        end = len(piles)
        piles.sort(reverse=True)

        total = 0

        while ((end - start) >= 1):
            total += piles[start + 1]
            start += 2
            end -= 1


        return total
