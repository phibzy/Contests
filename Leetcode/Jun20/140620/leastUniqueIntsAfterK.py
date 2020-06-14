#!/usr/bin/python3

"""

Given an array of integers arr and an integer k.

Find the least number of unique integers after removing exactly k elements.

"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # remember k=0 case
        freq = dict()        
        
        for i in arr:
            if i in freq:
                freq[i] += 1
            
            else:
                freq[i] = 1
        
        freq = {key: val for key,val in sorted(freq.items(), key=lambda item: item[1])}
        
        for key,val in list(freq.items()):
            if (val - k) <= 0:
                k = k - val
                del freq[key]
            
            else: break
        
        return len(freq)
