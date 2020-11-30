#!/usr/bin/python3

"""
    Test Cases:
        - Output with only 1 element
        - k = 0
        - List in decreasing order
        - Random cases



    Tests are wrong

    k is the length of the resulting subsequence

"""

import unittest
from mostComp import Solution

class testMostComp(unittest.TestCase):

    a = Solution()

    def testK0(self):
        self.assertEqual(self.a.mostCompetitive([2,6,4,3,7,8,42,9], 8), [2,6,4,3,7,8,42,9])

    def test1ElementOutput(self):
        self.assertEqual(self.a.mostCompetitive([3,4,6,9,5,3,5,7,1,30,293,4,49,3,9,2,3,4], 1), [1])

    def test1ElementOutputSmall(self):
        self.assertEqual(self.a.mostCompetitive([5,3,20,9,2,30,6], 6), [3,20,9,2,30,6])

    def testListDecreasing(self):
        self.assertEqual(self.a.mostCompetitive([14,11,9,8,6,5,4,3,1], 4), [5,4,3,1])

    def testRandom1(self):
        self.assertEqual(self.a.mostCompetitive([7,6,2,3,4], 2), [2,3])

    def testRandom2(self):
        self.assertEqual(self.a.mostCompetitive([3,5,2,6], 2), [2,6])
