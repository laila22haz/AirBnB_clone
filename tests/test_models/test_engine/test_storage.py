#!/usr/bin/python3
"""
Unittest for Filestorage
"""
import unittest
from unittest.mock import MagicMock, patch
import os
import models
from datetime import datetime, timedelta
from time import sleep
from models import storage
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

def is_valis_id(id):
    try:
        uuid.UUID(id)
        return True
    except ValueError:
        return False

def converter(date_val):
    try:
        return date_val.strftime("datetime.datetime(%Y, %-m, %dT, %-H, %-M, %-S, %f)")
    except TypeError:
        return -1

class StorageTestCase(unittest.TestCase):
    """Test class for Filestorage"""
    @classmethod
    def setUp(cls):
        """set up class for to initialize test cases"""
        json_clear()
        cls.my_model = BaseModel()
        cls.id, cls.crt_date, cls.upd_date = dispatch(cls.my_model)
        cls.maxDiff = None
        
    @classmethod
    def tearDown(cls):
        """tear down class for to close test cases"""
        json_clear()

    def test_1_initials(self):
        """instanciation tests"""
        json_clear()
        self.assertTrue(isinstance(storage, models.FileStorage))
    