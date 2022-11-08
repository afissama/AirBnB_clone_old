#!usr/bin/python3
"""
This module contains Class Base model
That defines all common attributes and Methods for other
Classes
"""
from datetime import datetime
import uuid
import copy


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Called when a BaseModel object is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = copy.deepcopy(self.created_at)

    def __str__(self):
        """
        String representation of Base Model
        """
        return "[" + self.__class__.__name__ + \
            "] (" + self.id + ") " + str(self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of dict
        """
        temp = copy.deepcopy(self.__dict__)

        temp['__class__'] = self.__class__.__name__
        temp['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        temp['id'] = self.id
        temp['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return temp
