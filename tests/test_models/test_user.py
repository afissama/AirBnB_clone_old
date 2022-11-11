#!/usr/bin/python3
"""Module to test User model
"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test User Attributes
    """

    def test_email(self):
        """Test email
        """
        user = User()
        User.email = "my@enemy.com"
        self.assertEqual(user.email, "my@enemy.com")
        self.assertEqual(User.email, "my@enemy.com")
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """Test password
        """
        user = User()
        User.password = "password.com"
        self.assertEqual(user.password, User.password)
        self.assertEqual(str, type(User.password))
        self.assertIsNotNone(User.password)
