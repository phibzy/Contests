#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 30, 2020 13:03:06 AEST
  @file        : q1

"""

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i = 0
        j = m
        
        if k*m > len(arr): return False
        if k == 1: return True;
        
        pattern = arr[0:m]
        oldI = (0, m)
        count = 1
        
        i += m
        j += m
        
        while j <= len(arr):
            print(f"Current pattern is: {pattern}, comparing with {arr[i:j]}")
            if pattern == arr[i:j]:
                print("a match")
                count += 1
                if count == k: return True
            
            else:
                print("not a match")
                i = oldI[0] + 1
                j = oldI[1] + 1
                pattern = arr[i:j]
                oldI = (i, j)
                count = 1
            
            i += m
            j += m
            
        return False
