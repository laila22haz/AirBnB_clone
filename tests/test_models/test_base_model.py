#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import unittest
import os
from datetime import datetime, timedelta
from models.base_model import BaseModel
import uuid


def json_clear():
    json_file = [file for file in os.listdir(os.getcwd())
                 if file.endswith(".json")]
    for file in json_file:
        file_path = os.path.join(os.getcwd(), file)
        os.remove(file_path)
        print(f"{file} removed...")


def dispatch(obj):
    if isinstance(obj, BaseModel):
        return [obj.id, obj.created_at, obj.updated_at]
    return []


def is_valid_id(id):
    try:
        uuid.UUID(id)
        return True
    except ValueError:
        return False


def converter(date_val):
    try:
        return date_val.strftime("datetime.datetime\
            (%Y, %-m, %dT, %-H, %-M, %-S, %f)")
    except TypeError:
        return -1


class BaseTestCase(unittest.TestCase):
    """Test class for BaseModel"""

    @classmethod
    def setUp(cls):
        """set up class to initialize test cases"""
        json_clear()
        cls.my_model = BaseModel()
        cls.id, cls.crt_date, cls.upd_date = dispatch(cls.my_model)
        cls.maxDiff = None

    @classmethod
    def tearDown(cls):
        """tear down class to close test cases"""
        json_clear()

    def assertDatetimeAlmostEqual(self, dt1, dt2,
                                  delta=timedelta(milliseconds=1000)):
        diff = abs(dt2 - dt1)
        self.assertTrue(diff <= delta, f"Difference between \
                        {dt1} and {dt2} is greater than {delta}")

    def assertDateGreater(self, d_upd, d_creat):
        self.assertTrue(d_upd >= d_creat, f"{d_creat} is more recent")

    def test_1_simple_initial_tests(self):
        """test case for attributes type and validity"""
        id, crt_date, upd_date = dispatch(self.my_model)
        self.assertEqual(type(self.my_model), BaseModel)
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertTrue(is_valid_id(self.my_model.id))
        self.assertEqual(self.my_model.id, id)
        self.my_model.id = 5
        self.assertEqual(self.my_model.id, 5)

    def test_2_datetime(self):
        """test cases for datetime attributes"""
        self.assertEqual(type(self.crt_date), datetime)
        self.assertEqual(type(self.upd_date), datetime)
        current = datetime.now()
        self.assertDatetimeAlmostEqual(self.crt_date, current)
        self.assertDateGreater(self.upd_date, self.crt_date)
        self.my_model.save()
        upd_date2 = self.my_model.updated_at
        current = datetime.now()
        self.assertDateGreater(upd_date2, self.crt_date)
        self.assertDatetimeAlmostEqual(current, upd_date2)

    def test_4_dict_representation(self):
        """test case for dict representations"""
        BaseDict = self.my_model.to_dict()
        self.assertEqual(type(BaseDict), dict)
        self.assertDictEqual({'__class__': 'BaseModel',
                              'id': self.id,
                              'created_at': self.crt_date.isoformat(),
                              'updated_at': self.upd_date.isoformat()},
                             BaseDict)

    def test_5_inst_from_dict(self):
        """test instantiation from dictionary"""
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        BaseDict = self.my_model.to_dict()
        new_model = BaseModel(**BaseDict)
        self.assertEqual(type(new_model), BaseModel)
        NewDict = new_model.to_dict()
        self.assertDictEqual({'__class__': 'BaseModel',
                              'id': self.id,
                              'created_at': self.crt_date.isoformat(),
                              'updated_at': self.upd_date.isoformat(),
                              'name': "My_First_Model",
                              'my_number': 89},
                             NewDict)
