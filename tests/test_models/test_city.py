#!/usr/bin/python3
"""Module for state Unittest"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """City testing class

    Args:
        unittest (_type_): _description_
    """
    def test_instancetype(self):
        """Unittest Class"""
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)
