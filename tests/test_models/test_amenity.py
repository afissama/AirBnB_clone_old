#!/usr/bin/python3
"""Module for state Unittest"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity testing class

    Args:
        unittest (_type_): _description_
    """
    def test_instancetype(self):
        """Unittest Class"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
