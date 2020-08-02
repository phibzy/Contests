#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 02, 2020 12:44:51 AEST
  @file        : q2

"""

from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        count = 0
        
        while count < k:
            if q[1] > q[0]:
                count = 1
                q.append(q[0])
                q.popleft()
                
            else:
                count += 1
                q.append(q[1])
                temp = q.popleft()
                q.popleft()
                q.appendleft(temp)
                
            if count >= len(arr): break
            
        return q[0]


