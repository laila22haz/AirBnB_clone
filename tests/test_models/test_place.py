#!/usr/bin/python3
"""
Unittest for the Place class
"""
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Test Place class"""
    def setUp(self):
        """method that setUp the Place"""
        self.place = Place()
        self.user = User()
        self.city = City()
        self.amenity = Amenity()

    def tearDown(self):
        """method that delete the Place"""
        del self.place

    def test_empty(self):
        """method that test if the attributes are empty"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(City, BaseModel))

    def test_assignment(self):
        """method that assign the attributes"""
        city_id_value = self.city.id
        user_id_value = self.user.id
        name_value = "89745924"
        description_value = "good_place"
        number_rooms_value = 7854955
        number_bathrooms_value = 87953
        max_guest_value = 789456
        price_by_night_value = 1000
        latitude_value = 1000.50
        longitude_value = 800.87
        amenity_ids_value = [self.amenity.id]

        self.place.city_id = city_id_value
        self.place.user_id = user_id_value
        self.place.name = name_value
        self.place.description = description_value
        self.place.number_rooms = number_rooms_value
        self.place.number_bathrooms = number_bathrooms_value
        self.place.max_guest = max_guest_value
        self.place.price_by_night = price_by_night_value
        self.place.latitude = latitude_value
        self.place.longitude = longitude_value
        self.place.amenity_ids = amenity_ids_value

        self.assertEqual(self.place.city_id, city_id_value)
        self.assertEqual(self.place.user_id, user_id_value)
        self.assertEqual(self.place.name, name_value)
        self.assertEqual(self.place.description, description_value)
        self.assertEqual(self.place.number_rooms, number_rooms_value)
        self.assertEqual(self.place.max_guest, max_guest_value)
        self.assertEqual(self.place.price_by_night, price_by_night_value)
        self.assertEqual(self.place.latitude, latitude_value)
        self.assertEqual(self.place.longitude, longitude_value)
        self.assertEqual(self.place.amenity_ids, amenity_ids_value)


if __name__ == '__main__':
    unittest.main()
