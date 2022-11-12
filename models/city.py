#!/usr/bin/python3
"""
City Representation module 
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a City
    Inherit from base model
    """
    
    state_id = ""
    name = ""

