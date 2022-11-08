#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time

class TestBase(unittest.TestCase):
    """
    Some functions to test the base class
    """

    def test_assigning_auto_id(self):
        """test base if not define id"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_current_date(self):
        """
        Test current date value
        """
        base1 = BaseModel()
        self.assertEqual(base1.created_at.replace(microsecond=0), datetime.today().replace(microsecond=0))

    def test_update_date(self):
        """
        Test update date value
        """
        base1 = BaseModel()
        self.assertEqual(base1.update_at.replace(microsecond=0), datetime.today().replace(microsecond=0))

    def test_update_after_save_date(self):
        """
        Test update date value
        """
        base1 = BaseModel()
        time.sleep(2)
        base1.save()
        self.assertEqual(base1.update_at.replace(microsecond=0), datetime.today().replace(microsecond=0))

    def test_to_dict(self):
        """
        Test update date value
        """
        import copy

        base1 = BaseModel()
        _to_dict = copy.deepcopy(base1.__dict__)

        _to_dict['__class__'] = "BaseModel"
        _to_dict['update_at'] = base1.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        _to_dict['id'] = base1.id
        _to_dict['created_at'] = base1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        _to_dict['__class__'] = base1.__class__.__name__
        self.assertDictEqual(base1.to_dict(), _to_dict)

    def test_to_str(self):
        """
        Test string representation value
        """
        base1 = BaseModel()

        _to_str = "[" + base1.__class__.__name__ + \
            "] (" + base1.id + ") " + str(base1.__dict__)
        self.assertEqual(str(base1), _to_str)
