#!/usr/bin/python3
"""
File Storage Module that serializes instances to a JSON
file and deserializes JSON file to instances.
"""
from models.base_model import BaseModel
import os
import json


class FileStorage:
    """
    Serializes instances to a JSON
    file and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the private dict __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + "."
                              + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """

        dict_ob = FileStorage.__objects
        objTodict = {key: dict_ob[key].to_dict() for key in dict_ob.keys()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objTodict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        if (not os.path.isfile(FileStorage.__file_path)):
            return

        with open(FileStorage.__file_path, encoding="utf-8") as f:
            loads_obj = json.load(f)
            for obj in loads_obj.values():
                self.new(eval(obj["__class__"])(obj))
