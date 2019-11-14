#!/usr/bin/python3
"""
    Unit test base model
"""
import unittest
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """test base model
    """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base_model.py"
        file2 = "tests/test_models/test_base_model.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 1,
                         "Found code style errors (and warning).")

    def test_doc(self):
        """Check the documentation"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        test_model = BaseModel()
        test_model.name = "AirBnBclone"
        test_model.my_number = 89
        a = test_model.to_dict()
        exp_att = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(a.keys(), exp_att)
        self.assertEqual(a['__class__'], 'BaseModel')
        self.assertEqual(a['name'], "AirBnBclone")
        self.assertEqual(a['my_number'], 89)

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
