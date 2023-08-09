#!/usr/bin/python3
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
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        k = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[k] = obj

    def save(self):
        obj_dict = {k: v.to_dict() for k,v in FileStorage.__objects.items()}        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        json_file = FileStorage.__file_path
        if os.path.exists(json_file):
            with open(json_file, "r") as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    name = obj["__class__"]
                    self.new(globals()[name](**obj))