#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Jul 05, 2020 12:45:53 AEST
  @file        : antPlank

"""

class Solution:
    def getLastMoment(self, n, left, right):
        # realLeft = [0]*(n+1)
        # for i in left:
            # realLeft[i] = 1

        # realRight = [0]*(n+1)
        # for i in right:
            # realRight[i] = 1

        """
        Base case: left array is at position n, delete
                   right array is at position 0, delete

        General case:
                First pass: if ant in front of you is facing you, turn around
                            Ants that turn around don't make another move
                Second pass: if ant is in same place as you, turn around
                update lists accordingly

        """


        """
        The ants literally walk through each other
        Don't keep track of who's who

        """
        if not left:
            retVal = right[-1]
        
        if not right:
            retVal = n - left[0]
            
        if right and left:
            retVal = max(n - left[0], right[-1])
            
        return retVal       





