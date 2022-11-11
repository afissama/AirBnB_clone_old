#!/usr/bin/python3
"""User Module to represent an User
"""
from models.base_model import BaseModel

class User(BaseModel):
    """User Class
        Public attrs:
            email: str
            password: str
            firstname: str
            last_name: str
    """

    def __init__(self, *args, **kwargs):
        """Call when instantiate the object"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if len(kwargs):
            super().__init__(**kwargs)
            return
        super().__init__()
