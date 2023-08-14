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


def dispatch(obj):
    if isinstance(obj, BaseModel):
        return [obj.id, obj.created_at, obj.updated_at]
    return []


class StorageTestCase(unittest.TestCase):
    """Test class for Filestorage"""
    maxDiff = None

    def test_1_initials(self):
        """instanciation tests"""
        jsonfile = "file.json"
        storage.clear()
        self.assertTrue(isinstance(storage, models.FileStorage))
        self.assertEqual(storage.all(), {})
        storage.reload()
        self.assertEqual(storage.all(), {})
        self.assertFalse(os.path.exists(jsonfile))
        mymodel = BaseModel()
        mymodel.save()
        self.assertTrue(os.path.exists(jsonfile))

    @patch('models.engine.file_storage.FileStorage.new')
    def test_2_new_method_called(self, mock_new):
        """test if new method is called when BaseModel instance is created"""
        mymodel = BaseModel()
        mock_new.assert_called_once_with(mymodel)

    @patch('models.engine.file_storage.FileStorage.save')
    def test_4_save_method_called(self, mock_save):
        """test if save method is called"""
        mymodel = BaseModel()
        mymodel.save()
        mock_save.assert_called_once()

    def test_5_save(self):
        """test save method with BaseModel"""
        storage.clear()
        mymodel = BaseModel()
        mymodel.save()
        id, crt, upd = dispatch(mymodel)
        StorageDict = storage.all()
        self.assertDictEqual({f"BaseModel.{mymodel.id}": mymodel}, StorageDict)


if __name__ == "__main__":
    unittest.main()
