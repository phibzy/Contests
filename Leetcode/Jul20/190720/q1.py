#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jul 19, 2020 12:28:41 AEST
  @file        : q1

"""

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        if numExchange > numBottles: return numBottles
        
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            calc = empty // numExchange
            total += calc
            empty = calc + (empty % numExchange)
            
        return total
