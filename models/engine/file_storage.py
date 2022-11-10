#!/usr/bin/python3
"""
File Storage Module that serializes instances to a JSON
file and deserializes JSON file to instances.
"""
import os
import json


class FileStorage:
    """
    Serializes instances to a JSON 
    file and deserializes JSON file to instances:
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """
        Returns the private dict __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with 
        key <obj class name>.id
        """
        __objects[obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file 
        (path: __file_path)
        """

        with open(__file_path, 'w', encoding="utf-8") as f:
            json.dump(__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        if (not os.path.isfile(__file_path)):
            return

        with open(__file_path, encoding="utf-8") as f:
            return json.load(f)
