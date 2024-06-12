#!/usr/bin/python3
import unittest
from models.user import User
import datetime

"""Defines a class TestAmenity"""

class TestUser(unittest.TestCase):
    """Class used for test cases"""
    def test_user(self):
        """Test case for Amenity"""
        self.user = User()
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
