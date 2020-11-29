#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Nov 29, 2020 13:45:47 AEDT
  @file        : mostComp

"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(msg)s")

class Solution:
    def mostCompetitive(self, nums, k):

        # Find lowest number that not in last (len - K) elements
        # and it's index, then rest of returned array is sorted
        # elements after it

        # Repeat for remaining list

        # if k==0, the substring is length of list, meaning
        # there's no competitors
        if k == 0: return nums


        # Brute force-y: Find min element and it's index with enough space at end
        #                Add to output, update list, repeat

        output = list()

        while k > 0 and k < len(nums):
            minVal, index = float('inf'), 0
            i = 0
            endPost = len(nums) - k

            while i <= endPost:
                
                if nums[i] < minVal:
                    minVal = nums[i]
                    index = i

                i += 1

            # Once found, trim list, update output
            output.append(minVal)
            nums = nums[index+1:]
            k -= 1

        if k != 0: output += nums

        return output













