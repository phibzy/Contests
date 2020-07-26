#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jul 26, 2020 12:29:21 AEST
  @file        : q1

"""

class Solution:
    def restoreString(self, s, indices):
        newS = ['']*len(s)
        for i, newI in enumerate(indices):
            newS[newI] = s[i]
        
        return ''.join(newS)
