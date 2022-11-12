#!/usr/bin/python3
"""
Amenity Representation module 
"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent a state
    Inherit from base model
    """
    
    name = ""
