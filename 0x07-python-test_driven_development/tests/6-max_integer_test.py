#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unitestest cases finding the max integer
    """
    def test_max(self):
        """
        Unitest cases positive numbers
        """
        self.assertEqual(max_integer([18, 2, 3, 89]), 89)
        self.assertEqual(max_integer([1, 55, 13, 7]), 55)

    def test_none(self):
        """
        Unitests with None return and raise None
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertRaises(TypeError, max_integer, None)
        self.assertAlmostEqual(max_integer([]), None)

    def test_float(self):
        """
        Unitests with floats values
        """
        self.assertAlmostEqual(max_integer([5.98, 7.95, 1.89]), 7.95)

    def test_tupla(self):
        """
        Unitest with a tuple
        """
        self.assertAlmostEqual(max_integer((6, 12, 24)), 24)

    def test_max_neg(self):
        """
        Unitest cases finding the max with negative numbers
        """
        self.assertEqual(max_integer([-4, -8, -3, -5]), -3)
        self.assertEqual(max_integer([-14, 5, -7]), 5)
