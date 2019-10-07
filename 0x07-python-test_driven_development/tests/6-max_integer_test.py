#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

        def test1(self):
                self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        def test2(self):
                with self.assertRaises(TypeError):
                        max_integer([10, (20, 30)])

        def test3(self):
                with self.assertRaises(TypeError):
                        max_integer(["casa", 3])

        def test4(self):
                self.assertEqual(max_integer([]), None)

        def test5(self):
                self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


if __name__ == '__main__':
        unittest.main()
