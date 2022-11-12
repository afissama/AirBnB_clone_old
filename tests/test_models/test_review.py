#!/usr/bin/python3
"""Module for state Unittest"""
import unittest
from models.review import Review


class TestCity(unittest.TestCase):
    """Review testing class

    Args:
        unittest (_type_): _description_
    """
    def test_instancetype(self):
        """Unittest Class"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
