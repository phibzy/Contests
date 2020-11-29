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

        location = dict()

        for i, v in enumerate(nums):
            location.setdefault(v, list())
            location[v].append(i)

        # sort list, then find smallest num
        sortedNums = sorted(nums)

        output = list()

        logging.debug(f"nums: {nums}")
        logging.debug(f"sortedNums: {sortedNums}")
        logging.debug("".rjust(20, "#"))

        modifier = 0

        while k > 0 and k < len(nums):
            # keep checking is <= endCheck
            endCheck = len(nums) - k
            found = False

            i = 0
            logging.debug(f"sortedNums: {sortedNums}")
            logging.debug(f"location[sortedNums[0]]: {location[sortedNums[0]]}")
            while i < len(location[sortedNums[0]]):
                nextLoc = location[sortedNums[0]][i] - modifier

                logging.debug(f"smallest: {sortedNums[0]}, nextLoc: {nextLoc}")
                logging.debug(f"i: {i}, endCheck: {endCheck}")

                del location[sortedNums[0]][i]

                if  nextLoc <= endCheck:
                    output.append(sortedNums[0])
                    
                    # Don't care about anything before
                    lenDiff = len(nums) - len(nums[nextLoc+1:])
                    nums = nums[nextLoc+1:]
                    sortedNums = sorted(nums)
                    k -= 1
                    found = True
                    modifier += lenDiff
                    break
            
            if not found: del sortedNums[0]

            logging.debug(f"k: {k}")
            logging.debug(f"nums: {nums}")
            logging.debug(f"sortedNums: {sortedNums}")
            logging.debug(f"output: {output}")
            logging.debug("".rjust(20, "#"))
            logging.debug("".rjust(20, "#"))

        if k != 0: output += nums

        return output

a = Solution()

a.mostCompetitive([2,4,3,3,5,4,9,6],4)
