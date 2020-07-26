#!/usr/bin/python3

"""
   Test Cases:

    - All alternating digits
    - All 1s
    - All 0s
    - Example case
    - End starts with 0s, 1s in the middle


"""

import unittest
from q2 import Solution

class testFlips(unittest.TestCase):

   a = Solution()

   def test0000000(self):
       self.assertEqual(self.a.minFlips('0000000'), 0, "Fails 000000 case")

   def test0(self):
       self.assertEqual(self.a.minFlips('0'), 0, "Fails 0 case")

   def test1(self):
       self.assertEqual(self.a.minFlips('1'), 1, "Fails 1 case")

   def test111111(self):
       self.assertEqual(self.a.minFlips('1111111111'), 1, "Fails 1111111 case")

   def testExample(self):
       self.assertEqual(self.a.minFlips('1111111111'), 1, "Fails 1111111 case")

   def test1sInMiddle(self):
       self.assertEqual(self.a.minFlips('0001110000'), 2, "Fails 1s in middle case")

   def testAlternating1(self):
       self.assertEqual(self.a.minFlips('010101010101'), 11, "Fails alternating1 case")

   def testAlternating2(self):
       self.assertEqual(self.a.minFlips('101010101010'), 12, "Fails alternating2 case")

   def testExample2(self):
       self.assertEqual(self.a.minFlips("001011101"), 5, "Fails Example2 case")

