#!/usr/bin/python3
"""
    Unit test base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test base model
    """

    def test_objects(self):
        """test objects comparison"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_instances(self):
        """test instance of the class and attributes instances of data type"""
        obj1 = BaseModel()
        self.assertIsInstance(obj1.id, str)
        self.assertIsInstance(obj1, BaseModel)

    def test_id(self):
        """test id"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, 'id'))

if __name__ == '__main__':
    unittest.main()
