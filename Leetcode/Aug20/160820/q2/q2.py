#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 16, 2020 13:53:00 AEST
  @file        : q2

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

"""

class Solution:
    def minOperations(self, n: int) -> int:
        # based around middle element
        # want to add to first, subtract from last and keep going in
        # Beware of even case
        # Case 1: if only 1 element return 0
        if n == 1: return 0
                
        median = 2 * (n // 2) + 1
        median -= (n % 2 == 0)
        
        smallest = 1
        total = 0
        
        while smallest < median:
            total += (median - smallest)
            smallest += 2            
        
        return total
    
