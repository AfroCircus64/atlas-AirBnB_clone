#!usr/bin/python3
import unittest
from models.amenity import Amenity
import datetime

"""Defines a class TestAmenity"""

class TestAmenity(unittest.TestCase):
    """Class used for test cases"""
    def test_amenity(self):
        """Test case for Amenity"""
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")
