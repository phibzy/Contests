#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jul 26, 2020 12:37:15 AEST
  @file        : q2

"""

# Cheesy algo: start from end, if 1 add one, keep going until reach end or zero
               # If encounter 0 then keep going until you reach end or one
               # If encounter 1 then add 2 to the count

# Bit shifting approach too
# XOR approach

class Solution:
    def minFlips(self, target):
        end = len(target) - 1

        count = int(target[end])
        flag = target[end]
        end -= 1
        while end >= 0:
            if target[end] != flag:
                count += [2,0][int(flag)]
                flag = target[end]

            end -= 1

        return count

