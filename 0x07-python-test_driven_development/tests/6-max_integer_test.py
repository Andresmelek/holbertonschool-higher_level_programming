#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def check_max(self):
        """
        Checks if gets the max number
        """
        self.assertAlmostEqual(max_integer([18, 89, 05]), 89)
        self.assertAlmostEqual(max_integer([-5, -1, -8]), -1)
        self.assertAlmostEqual(max_integer([0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
