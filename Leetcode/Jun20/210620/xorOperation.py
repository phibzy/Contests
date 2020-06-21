#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jun 21, 2020 20:35:21 AEST
  @file        : xorOperation

"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        result = 0
        
        for i in range(n):
            result ^= (start + 2*i)
            
        return result
