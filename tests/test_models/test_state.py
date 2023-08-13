#!/usr/bin/python3
"""
Unittest for the State class
"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """Test State class"""
    def setUp(self):
        """method that setUp the State"""
        self.state = State()

    def tearDown(self):
        """method that delete the review"""
        del self.state

    def test_empty(self):
        """method that test if the attributes are empty"""
        self.assertEqual(self.state.name, "")

        self.assertTrue(issubclass(State, BaseModel))

    def test_assignment(self):
        """method that assign the attributes"""
        name_value = "Ouarzazate"

        self.state.name = name_value

        self.assertEqual(self.state.name, name_value)


if __name__ == '__main__':
    unittest.main()
