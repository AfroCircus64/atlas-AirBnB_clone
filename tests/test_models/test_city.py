#!/usr/bin/python3
import unittest
from models.city import City
import datetime

"""Defines a class TestCity"""


class TestCity(unittest.TestCase):
    """Class used for test cases"""
    def test_city(self):
        """Test case for City"""
        self.city = City()
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.name, "")
