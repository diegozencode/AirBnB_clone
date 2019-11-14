#!/usr/bin/python3
"""
    Unit test base model
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test amenity"""

    def test_instance(self):
        """test instance of the class and attributes instance of data type"""
        obj1 = Amenity()
        self.assertIsInstance(obj1.name, str)
        self.assertIsInstance(obj1, Amenity)

    def test_name(self):
        """test name"""
        obj1 = Amenity()
        self.assertTrue(hasattr(obj1, 'name'))

if __name__ == '__main__':
    unittest.main()
