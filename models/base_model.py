#!usr/bin/python3
"""
This module contains Class Base model
That defines all common attributes and Methods for other
Classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Called when a BaseModel object is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        String representation of Base Model
        """
        return "[" + self.__class__.__name__ + \
            "] (<" + self.id + ">) <" + str(self.__dict__) + ">"

    def save(self):
        """
        Updates the public instance attribute
        update_at with the current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of dict
        """
        temp = self.__dict__
        temp['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        temp['update_at'] = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        temp['__class__'] = self.__class__.__name__
        return temp
