#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 22, 2020 14:29:14 AEDT
  @file        : stringEqual

"""

# didn't bother with tests since this is
# a simple one liner in python

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
