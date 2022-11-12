#!/usr/bin/python3
"""Module for state Unittest"""
import unittest
from models.place import Place


class TestCity(unittest.TestCase):
    """City testing class

    Args:
        unittest (_type_): _description_
    """
    def test_instancetype(self):
        """Unittest Class"""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
