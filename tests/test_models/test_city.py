#!/usr/bin/python3
"""Unittest for the City class
"""
from models.city import City
from models.state import State
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Test city class"""
    def setUp(self):
        """method that setUp the city"""
        self.state = State()
        self.city = City()

    def tearDown(self):
        """method that delete the city"""
        del self.city

    def test_empty(self):
        """method that test if the attributes are empty"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

        self.assertTrue(issubclass(City, BaseModel))

    def test_assignment(self):
        """method that assign the attributes"""
        state_id_value = self.state.id
        self.city.email = state_id_value
        name_value = "Ouarzazate"
        self.city.password = name_value

        self.assertEqual(self.city.email, state_id_value)
        self.assertEqual(self.city.password, name_value)


if __name__ == '__main__':
    unittest.main()
