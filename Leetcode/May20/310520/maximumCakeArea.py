#!/usr/bin/python3

class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        # Make sure both lists are sorted
        horizontalCuts.sort()
        verticalCuts.sort()

        print(horizontalCuts)
        print(verticalCuts)
        
        maxHeight = self.biggestInterval(h, horizontalCuts)
        maxWidth  = self.biggestInterval(w, verticalCuts)
        
        print(f"maxHeight is {maxHeight}, maxWidth is {maxWidth}, maxH * maxW is {maxHeight * maxWidth}")

        rVal = (maxHeight * maxWidth) % (10**9 + 7)
        
        return rVal
        
    def biggestInterval(self, h, horizontalCuts):

        print(''.center(20, '-'))
        print(f"Dealing with list: {horizontalCuts} with maxBound {h}")
        print(''.center(20, '-'))
        
        maxHeight = horizontalCuts[0]
        print(f"rVal is {maxHeight}")
        
        prev = 0
        for i in range(1, len(horizontalCuts)):
            result = horizontalCuts[i] - horizontalCuts[prev]
            print(f"result is: {horizontalCuts[i]} - {horizontalCuts[prev]} = {result}")
            if result > maxHeight: maxHeight = result
            print(f"rVal is {maxHeight}")
            prev += 1
        
        # check end element
        result = h - horizontalCuts[-1]
        print(f"result is: {h} - {horizontalCuts[-1]} = {result}")
        maxHeight = max(maxHeight, result)
        print(f"rVal is {maxHeight}")
        
        return maxHeight

a = Solution()

print(a.maxArea(50, 15, [37,40,41,30,27,10,31], [2,1,9,5,4,12,6,13,11]))

