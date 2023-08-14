#!/usr/bin/python3
"""
Unittest for the Amenity class
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""
    def setUp(self):
        """method that setUp the Amenity"""
        self.amenity = Amenity()

    def tearDown(self):
        """method that delete the Amenity"""
        del self.amenity

    def test_empty(self):
        """method that test if the attributes are empty"""
        self.assertEqual(self.amenity.name, "")

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_assignment(self):
        """method that assign the attributes"""
        name_value = "Hair_Salon"
        self.amenity.name = name_value

        self.assertEqual(self.amenity.name, name_value)


if __name__ == '__main__':
    unittest.main()
