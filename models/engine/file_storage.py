#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
"""Build storage class"""


class FileStorage():
    """Class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        new_dict = {}  # First, when an instance of MyBase is created, it will be passed
        for key, value in self.__objects.items():
            # into save_to_dict() method that converts this instance or object to a Python dictionary representation.
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            # The dictionary representation will then be passed into the Python JSON module, which uses the Json.dump() function to convert the dictionary representation to a JSON string, which is subsequently written into a file.
            json.dump(new_dict, file, indent=4)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    name = value["__class__"]
                    name_exist = globals().get(name)
                    if name_exist:
                        self.new(name_exist(**value))
        except FileNotFoundError:
            pass
