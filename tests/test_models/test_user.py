#!/usr/bin/python3
"""Module to test User model
"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test User Attributes
    """

    def test_mail(self):
        user = User()
        User.email = "my@enemy.com"
        self.assertEqual(user.email, "my@enemy.com")
