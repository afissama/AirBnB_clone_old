#!/usr/bin/python3
"""
Unittest for filestorage method
"""
import json
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test FileStorage method
    """

    def test_objs(self):
        """
        Test file storage instantiation
        """

    def test_all(self):
        """
        Test all
        """
        base = BaseModel()
        objs = models.storage.all()
        self.assertEqual(type(objs), dict)

    def test_new(self):
        """
        Test new
        """
        base = BaseModel()
        tmp_storage = FileStorage()
        tmp_storage.new(base)
        objs = models.storage.all()
        self.assertEqual(type(objs), dict)
        self.assertTrue("BaseModel.{}".format(base.id) in objs.keys())

    def test_save(self):
        """
        """
        if (os.path.isfile("file.json")):
            os.remove("file.json")

        base_0 = BaseModel()
        base_1 = BaseModel()
        tmp_storage = FileStorage()
        tmp_storage.new(base_0)
        tmp_storage.new(base_1)
        tmp_storage.save()

        self.assertTrue(os.path.isfile("file.json"))
        loads_obj = {}
        with open("file.json", encoding="utf-8") as f:
            loads_obj = json.load(f)
        
        self.assertTrue("BaseModel.{}".format(base_0.id) in loads_obj.keys())
        self.assertTrue("BaseModel.{}".format(base_1.id) in loads_obj.keys())

    def test_reload(self):
        """
        Test the reload func
        """
        if (os.path.isfile("file.json")):
            os.remove("file.json")

        base_0 = BaseModel()
        base_1 = BaseModel()
        models.storage.new(base_0)
        models.storage.new(base_1)
        models.storage.save()
        models.storage.reload()
        loads_obj = models.storage.all()
        self.assertTrue("BaseModel.{}".format(base_0.id) in loads_obj.keys())
        self.assertTrue("BaseModel.{}".format(base_1.id) in loads_obj.keys())

    def test_reload_no_file(self):
        """
        Reload
        """
        objs = models.storage.all()
        models.storage.reload()
        self.assertEqual(objs, models.storage.all())

    def testFileStorage_objects_is_private_attribute(self):
        """
        Test if attribute is private
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_file_path_is_private_str(self):
        """
        Test if attribute is private
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))