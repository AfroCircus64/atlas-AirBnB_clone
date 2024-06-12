#!/user/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models import storage

"""Defines a class TestFileStorage"""


class TestFileStorage(unittest.TestCase):
    """Class used for test cases"""
    def setUp(self):
        """Set up a new BaseModel instance for each test."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.file_path = "file_test.json"
        storage.__file_path = self.file_path

    def tearDown(self):
        """tear down after each test"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all"""
        all_objects = self.storage.all()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.new(self.model)
        all_objects = self.storage.all()
        self.assertEqual(all_objects[key], self.model)
    
    def test_new(self):
        """Test the new method"""
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())
    
    def test_update(self):
        """Test the update method"""
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.new(self.model)
        new_value = "new_value"
        self.storage.update(self.model, 'test_attribute', new_value)
        updated_object = self.storage.all()[key]
        self.assertEqual(getattr(updated_object, 'test_attribute'), new_value)

    def test_remove(self):
        """Test the remove method"""
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.new(self.model)
        self.storage.remove(key)
        self.assertNotIn(key, self.storage.all())
    
    def test_save_and_reload(self):
        """Test the save and reload methods"""
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.new(self.model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        reloaded_object = new_storage.all()[key]
        self.assertNotEqual(reloaded_object.id, self.model.id)
        self.assertNotEqual(reloaded_object.to_dict(), self.model.to_dict())

    if __name__ == '__main__':
        unittest.main()
