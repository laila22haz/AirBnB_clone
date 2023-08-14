#!/usr/bin/python3
"""
Unittest for the Review class
"""
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """Test Review class"""
    def setUp(self):
        """method that setUp the Review"""
        self.review = Review()
        self.user = User()
        self.place = Place()

    def tearDown(self):
        """method that delete the review"""
        del self.review

    def test_empty(self):
        """method that test if the attributes are empty"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

        self.assertTrue(issubclass(Review, BaseModel))

    def test_assignment(self):
        """method that assign the attributes"""
        place_id_value = self.place.id
        user_id_value = self.user.id
        text_value = "Very_good_service"

        self.review.place_id = place_id_value
        self.review.user_id = user_id_value
        self.review.text = text_value

        self.assertEqual(self.review.place_id, place_id_value)
        self.assertEqual(self.review.user_id, user_id_value)
        self.assertEqual(self.review.text, text_value)


if __name__ == '__main__':
    unittest.main()
