#!/usr/bin/python3

"""
   Test Cases:

   - Example ones
   - Completely unbalanced tree with distance 2 and pretty lengthy


"""

import unittest
from q3 import Solution

class testQ3(unittest.TestCase):

   a = Solution()

   def testExample1(self):
       self.assertEqual(self.a.countPairs([1,2,3,None,4], 3), 1, "Fails example 1 case")

   def testExample2(self):
       self.assertEqual(self.a.countPairs([1,2,3,4,5,6,7], 3), 2, "Fails example 2 case")

   def testExample3(self):
       self.assertEqual(self.a.countPairs([7,1,4,6,None,5,3,None,None,None,None,None,2], 3), 1, "Fails example 3 case")

   def testExample4(self):
       self.assertEqual(self.a.countPairs([100], 1), 0, "Fails example 4 case")

   def testExample5(self):
       self.assertEqual(self.a.countPairs([1,1,1], 2), 1, "Fails example 5 case")

