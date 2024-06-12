#!/usr/bin/python3
import unittest
from models.state import State
import datetime

"""Defines a class TestState"""

class TestState(unittest.TestCase):
    """Class used for test cases"""
    def test_state(self):
        """Test case for State"""
        self.state = State()
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")
