#!/usr/bin/python3
"""
    Unit test place model
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """test place"""

    def test_instance(self):
        """test instance of the class and attributes instance of data type"""
        obj1 = Place()
        self.assertIsInstance(obj1.name, str)
        self.assertIsInstance(obj1.description, str)
        self.assertIsInstance(obj1.number_rooms, int)
        self.assertIsInstance(obj1.number_bathrooms, int)
        self.assertIsInstance(obj1.max_guest, int)
        self.assertIsInstance(obj1.price_by_night, int)
        self.assertIsInstance(obj1.latitude, float)
        self.assertIsInstance(obj1.longitude, float)
        self.assertIsInstance(obj1, Place)

    def test_name(self):
        """test name"""
        obj1 = Place()
        self.assertTrue(hasattr(obj1, 'name'))

if __name__ == '__main__':
    unittest.main()
