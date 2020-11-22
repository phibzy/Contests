#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 22, 2020 14:31:56 AEDT
  @file        : smallestStr

"""

# TC: O(N)
# SC: O(N)

class Solution:
    def getSmallestString(self, n, k):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        d = dict()
        i = 1
        
        for letter in alphabet:
            d[i] = letter
            i += 1
            
        # Use a stack for better time complexity
        s = list()
        st = ''

        # we work backwards
        # if there's any remainder from k-n, we know
        # that more than repeated a's are required
        # We simply check the difference, then add the difference
        # to a's value to get the char we need
        while n > 0:
            diff = (k - n)
           
            # Remember, if there's still more remainder left
            # we need to carry that forward for next calculations
            if diff >= 26:
                diff = 26
                
            else:
                diff = diff % 26 + 1
                
            s.append(d[diff])
            
            # Update value of k and n
            k -= diff
            n -= 1
       
        while s:
            st += s.pop()
            
        return st


