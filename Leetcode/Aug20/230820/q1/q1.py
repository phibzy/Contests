#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Aug 23, 2020 12:45:34 AEST
  @file        : q1

"""

class Solution:
    def mostVisited(self, n, rounds):
        sectors = [ 0 for _ in range(n + 1) ]

        sign = 1
        sectors[rounds[0]] = 1
        for i in range(len(rounds) - 1):
            if rounds[i+1] < rounds[i]: sign = -1
            print(f"i is {i}, rounds[i] + 1 is {rounds[i] + 1}, rounds[i+1] is {rounds[i+1]}")
            for j in range(rounds[i] + 1, rounds[i+1] + 1, sign):
                print(j);
                sectors[j] += 1
            sign = 1

        print(sectors)




a = Solution()
a.mostVisited(4, [1,3,1,2])
a.mostVisited(2, [2,1,2,1,2,1,2,1,2])
a.mostVisited(7, [1,3,5,7])
