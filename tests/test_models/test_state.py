#!/usr/bin/python3
"""Module for state Unittest"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State testing class

    Args:
        unittest (_type_): _description_
    """
    def test_instancetype(self):
        """Unittest Class"""
        state = State()
        self.assertIsInstance(state.name, str)
