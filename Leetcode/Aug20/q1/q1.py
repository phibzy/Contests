#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 02, 2020 12:05:31 AEST
  @file        : q1

"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if ((abs(arr[i] - arr[j]) <= a) and 
                       (abs(arr[j] - arr[k]) <= b) and 
                       (abs(arr[i] - arr[k]) <= c)):
                        count += 1
        
        return count
