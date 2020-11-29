#!/usr/bin/python3

"""
    Test Cases:
        - Basic quick tests


"""

import unittest
from maximumWealth import Solution

class testMW(unittest.TestCase):

    a = Solution()

    def test1(self):
        self.assertEqual(self.a.maximumWealth([[1,5],[7,3],[3,5]]), 10)

