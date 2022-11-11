#!/usr/bin/python3
"""Unittest for base class
"""
import os
import unittest
import models
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
        self.assertEqual(base1.created_at.replace(microsecond=0), datetime.utcnow().replace(microsecond=0))

    def test_update_date(self):
        """
        Test update date value
        """
        base1 = BaseModel()
        self.assertEqual(base1.updated_at.replace(microsecond=0), datetime.utcnow().replace(microsecond=0))

    def test_update_after_save_date(self):
        """
        Test update date value
        """
        base1 = BaseModel()
        time.sleep(1)
        base1.save()
        self.assertEqual(base1.updated_at.replace(microsecond=0), datetime.utcnow().replace(microsecond=0))

    def test_to_dict(self):
        """
        Test update date value
        """
        import copy

        base1 = BaseModel()
        _to_dict = copy.deepcopy(base1.__dict__)

        _to_dict['__class__'] = "BaseModel"
        _to_dict['updated_at'] = base1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
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

    def test_init_with_arg(self):
        """
        Test if **argv param
        is used as espected
        """
        if (os.path.isfile("file.json")):
            os.remove("file.json")

        base0 = BaseModel()
        base0.name = "TestCase"
        base0.age = "No"
        basejson = base0.to_dict()
    
        base1 = BaseModel(**basejson)
        self.assertEqual(base1.name, "TestCase")
        self.assertTrue("BaseModel.{}".format(base1.id) in models.storage.all())

    def test_save_withstorage(self):
        """
        Test if save worked as expected
        """
        if (os.path.isfile("file.json")):
            os.remove("file.json")

        base0 = BaseModel()
        base0.name = "TestCase"
        base0.age = "No"
        time.sleep(1)

        base0.save()
        models.storage.reload()
        objs = models.storage.all()
        self.assertEqual(objs["BaseModel.{}".format(base0.id)].updated_at, base0.updated_at)
    
    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())