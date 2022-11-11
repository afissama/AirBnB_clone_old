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
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Call when instantiate the object"""
        if len(kwargs):
            super().__init__(**kwargs)
            return
        super().__init__()
