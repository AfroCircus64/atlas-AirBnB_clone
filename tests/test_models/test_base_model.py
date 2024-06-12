#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
import os

"""Defines a class TestBaseModel"""


class TestBaseModel(unittest.TestCase):
    """Class used for test cases"""
    def setUp(self):
        """Set up a new BaseModel instance for each test."""
        self.model = BaseModel()

    def test_save(self):
        """Test the save()"""
        original_save = self.model.updated_at
        self.model.save()
        new_save = self.model.updated_at
        self.assertNotEqual(original_save, new_save)

    def test_to_dict(self):
        """Test the to_dict()"""
        model_dict = self.model.to_dict()
        self.assertTrue(type(model_dict["created_at"]) is str)
        self.assertTrue(type(model_dict) is dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_id(self):
        """Test the self.id"""
        self.assertTrue(type(self.model.id) is str)

    def test_created_at(self):
        """Test the self.created_at"""
        self.assertTrue(type(self.model.created_at) is datetime.datetime)

    def test_str(self):
        """Test the __str__(self)"""
        self.assertEqual(str(self.model), "[{}] ({})\
 {}".format(self.model.__class__.__name__, self.model.id, self.model.__dict__))

if __name__ == '__main__':
    unittest.main()
