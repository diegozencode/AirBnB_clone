#!/usr/bin/python3
"""
    Unit test review model
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test review"""

    def test_instance(self):
        """test instance of the class and attributes instance of data type"""
        obj1 = Review()
        self.assertIsInstance(obj1.text, str)
        self.assertIsInstance(obj1, Review)

    def test_attr(self):
        """test attribute"""
        obj1 = Review()
        self.assertTrue(hasattr(obj1, 'text'))

if __name__ == '__main__':
    unittest.main()
