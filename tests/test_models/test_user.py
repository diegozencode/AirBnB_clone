#!/usr/bin/python3
"""
    Unit test user model
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test user"""

    def test_instance(self):
        """test instance of the class and attributes instance of data type"""
        obj1 = User()
        self.assertIsInstance(obj1.email, str)
        self.assertIsInstance(obj1.password, str)
        self.assertIsInstance(obj1.first_name, str)
        self.assertIsInstance(obj1.last_name, str)
        self.assertIsInstance(obj1, User)

    def test_attr(self):
        """test attribute"""
        obj1 = User()
        self.assertTrue(hasattr(obj1, 'email'))
        self.assertTrue(hasattr(obj1, 'password'))
        self.assertTrue(hasattr(obj1, 'first_name'))
        self.assertTrue(hasattr(obj1, 'last_name'))

if __name__ == '__main__':
    unittest.main()
