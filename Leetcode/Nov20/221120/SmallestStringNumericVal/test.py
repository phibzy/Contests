#!/usr/bin/python3

"""
    Test Cases:
        - One letter
        - All a
        - Carry over

Future note: just skip the error message, testcase name
is more than enough info

"""

import unittest
from smallestStr import Solution

class test(unittest.TestCase):

    a = Solution()

    def testAllAs(self):
        self.assertEqual(self.a.getSmallestString(4,4), "aaaa", "fails case 1")

    def test2(self):
        self.assertEqual(self.a.getSmallestString(4,5), "aaab", "fails case 2")

    def test3(self):
        self.assertEqual(self.a.getSmallestString(4,30), "aabz", "fails case 3")

    def test4(self):
        self.assertEqual(self.a.getSmallestString(4,104), "zzzz", "fails case 4")

    def test5(self):
        self.assertEqual(self.a.getSmallestString(1,26), "z")
