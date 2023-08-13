#!/usr/bin/python3
"""
Unittest for User Class
"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Test User class"""
    def setUp(self):
        """method that setUp the user"""
        self.user = User()

    def tearDown(self):
        """method that delete the user"""
        del self.user

    def test_empty(self):
        """method that test if the attributes are empty"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

        self.assertTrue(issubclass(User, BaseModel))

    def test_assignment(self):
        """method that assign the attributes"""
        email_value = "test@gmail.com"
        self.user.email = email_value
        password_value = "azertyuiop"
        self.user.password = password_value
        first_name_val = "SponjBoB"
        self.user.first_name = first_name_val
        last_name_value = "AirBnB"
        self.user.last_name = last_name_value

        self.assertEqual(self.user.email, email_value)
        self.assertEqual(self.user.password, password_value)
        self.assertEqual(self.user.first_name, first_name_val)
        self.assertEqual(self.user.last_name, last_name_value)


if __name__ == '__main__':
    unittest.main()
