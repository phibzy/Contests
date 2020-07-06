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
        # Space complexity for both solutions is constant        
        
        # First solution: O(NlogN) since I use sort function
        #left.sort()
        #right.sort()
        
        #if not right:
        #    retVal = left[-1]
        
        #if not left:
        #    retVal = n - right[0]
            
        #if right and left:
        #    retVal = max(n - right[0], left[-1])
            
        #return retVal
    
        # Second Solution: O(N), since min/max functions are O(N)
        #if not left:
        #    return n - min(right)
        
        #if not right:
        #    return max(left)
        
        #return max(max(left), n - min(right))
        
        
        # One liner because you can
        return max(max(left, default=0), n - min(right, default=n))





