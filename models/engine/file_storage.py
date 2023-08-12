#!/usr/bin/python3
"""
FileStorage module to store data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class for storing and loading data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """stores an object on the objects dictionary"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[k] = obj

    def save(self):
        """saves the objects dictionary on a json file"""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """loads string repr of objects from json file"""
        json_file = FileStorage.__file_path
        if os.path.exists(json_file):
            with open(json_file, "r") as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    name = obj["__class__"]
                    self.new(globals()[name](**obj))
