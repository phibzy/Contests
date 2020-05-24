#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(msg)s")
logging.disable(logging.DEBUG)

class Solution:
    def maxVowels(self, s, k):
        startI = 0
        
        vowels = "aeiou"
        
        returnSum = 0
        slidingSum = 0
        
        # Get initial sum of vowels
        for i in range(k):
            if s[i] in vowels:
                slidingSum += 1
       
        logging.debug(f"Initial sum is: {slidingSum}")

        returnSum = slidingSum
        
        for i in range(k, len(s)):
            logging.debug(f"Initial iteration sum is: {slidingSum}")
            if s[startI] in vowels:
                slidingSum -= 1
            
            startI += 1
            
            if s[i] in vowels:
                slidingSum += 1
                if slidingSum > returnSum: returnSum = slidingSum
            logging.debug(f"Sum after slide is: {slidingSum}")
                    
        return returnSum

a = Solution()

print(a.maxVowels("leetcode", 3))
