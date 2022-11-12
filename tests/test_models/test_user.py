#!/usr/bin/python3
"""Module to test User model
"""
from models.base_model import BaseModel
from models.user import User
import unittest
import models


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

    def test_firstname(self):
        """
        Test first name
        attribue
        """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()

        all_objs = models.storage.all()

        user_id = "User.{}".format(my_user.id)
        loaded_user = all_objs[user_id]

        self.assertIn(user_id, all_objs.keys())
        self.assertEqual(my_user.email, loaded_user.email)
        self.assertEqual(my_user.password, loaded_user.password)
        self.assertEqual(my_user.first_name, loaded_user.first_name)
        self.assertEqual(my_user.last_name, loaded_user.last_name)

    def test_instance_param(self):
        """Test if all param are str"""

        my_user = User()
        self.assertIsInstance(my_user.email, str)
        self.assertIsInstance(my_user.password, str)
        self.assertIsInstance(my_user.first_name, str)
        self.assertIsInstance(my_user.last_name, str)
