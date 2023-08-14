#!/usr/bin/python3
"""
FileStorage module to store data
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import json
import os
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    FileStorage class for storing and loading data

    Attributes:
        __file_path (str): the file path of json file
        __objects (dict): A dictionary to store instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        stores an object on the objects dictionary
        Arguments:
            obj : The object to be stored.
        """
        k = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[k] = obj

    def save(self):
        """saves the objects dictionary on a json file"""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file, indent=4)

    def reload(self):
        """loads string repr of objects from json file"""
        json_file = FileStorage.__file_path
        if os.path.exists(json_file):
            with open(json_file, "r") as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    name = obj["__class__"]
                    self.new(globals()[name](**obj))

    def clear(self):
        """clears the dictionary of objects"""
        keys_to_delete = list(FileStorage.__objects.keys())
        for k in keys_to_delete:
            del FileStorage.__objects[k]
        json_files = [file for file in os.listdir(os.getcwd())
                      if file.endswith(".json")]
        if not json_files:
            return
        for file in json_files:
            file_path = os.path.join(os.getcwd(), file)
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error removing {file}: {e}")
