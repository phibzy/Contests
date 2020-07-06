#!/usr/bin/python3

"""
   Test Cases:



"""

import unittest
from antPlank import Solution

class testPlank(unittest.TestCase):

    a = Solution()

    def testAllRight(self):
        self.assertEqual(self.a.getLastMoment(7, [], [0,1,2,3,4,5,6,7]), 7)

    def testAllLeft(self):
        self.assertEqual(self.a.getLastMoment(7, [0,1,2,3,4,5,6,7], []), 7)

    def testExampleCase(self):
        self.assertEqual(self.a.getLastMoment(4, [0,1], [3,4]), 4)
