#!/usr/bin/python3
import unittest
from models.review import Review
import datetime

"""Defines a class TestReview"""


class TestReview(unittest.TestCase):
    """Class used for test cases"""
    def test_review(self):
        """Test case for Review"""
        self.review = Review()
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
