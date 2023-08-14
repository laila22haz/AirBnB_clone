#!/usr/bin/python3

"""Unittest for BaseModel
"""
import unittest
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models import storage
import uuid


def json_clear():
    json_file = [file for file in os.listdir(os.getcwd())
                 if file.endswith(".json")]
    for file in json_file:
        file_path = os.path.join(os.getcwd(), file)
        os.remove(file_path)


def dispatch(obj):
    if isinstance(obj, BaseModel):
        return [obj.id, obj.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')]
    return []


def is_valis_id(id):
    try:
        uuid.UUID(id)
        return True
    except ValueError:
        return False


class BaseTestCase(unittest.TestCase):
    """Test class for BaseModel"""
    @classmethod
    def setUpClass(cls):
        """set up class for to initialize test cases"""
        pass

    @classmethod
    def tearDownClass(cls):
        """tear down class for to close test cases"""
        pass

    def test_1(self):
        """test case for"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        id, crt_date, upd_date = dispatch(my_model)
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(is_valis_id(my_model.id))
        self.assertEqual(my_model.id, id)
        my_model.id = 5
        self.assertEqual(my_model.id, 5)
        self.assertEqual(str(my_model.created_at.
                         strftime('%Y-%m-%d %H:%M:%S')), crt_date)
        self.assertEqual(str(type(my_model.created_at)),
                         "<class 'datetime.datetime'>")
        self.assertEqual(str(my_model.updated_at.
                             strftime('%Y-%m-%d %H:%M:%S')), upd_date)
        self.assertEqual(str(type(my_model.updated_at)),
                         "<class 'datetime.datetime'>")
        self.assertEqual(str(my_model.created_at.
                             strftime('%Y-%m-%d %H:%M:%S')), current_date)
        sleep(1)
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        my_model.save()
        self.assertEqual(str(my_model.updated_at.
                         strftime('%Y-%m-%d %H:%M:%S')), current_date)

    def test_2(self):
        """test case for"""
        self.maxDiff = None
        my_model = BaseModel()
        self.assertEqual(str(type(str(my_model))), "<class 'str'>")
        dict_output = (
                f"[BaseModel] ({my_model.id}) "
                + "{{'id': '{}', ".format(my_model.id)
                + "'created_at': {}, "
                .format(my_model.created_at.strftime
                        ("datetime.datetime(%Y, %-m, %d, %-H, %-M, %-S, %f)"))
                + "'updated_at': {}"
                .format(my_model.updated_at.strftime
                        ("datetime.datetime(%Y, %-m, %d, %-H, %-M, %-S, %f)}"))
                )
        BaseDict = my_model.to_dict()
        self.assertDictEqual({'__class__': 'BaseModel',
                              'id': my_model.id,
                              'created_at': my_model.created_at.isoformat(),
                              'updated_at': my_model.updated_at.isoformat()},
                             BaseDict)
