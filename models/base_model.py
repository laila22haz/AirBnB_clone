#!/usr/bin/python3
"""Let's build the Base class"""


from datetime import datetime
import models
import uuid

class BaseModel():
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
               for key, value in kwargs.items():
                     if key != '__class__':
                        setattr(self, key, value)
               self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
               self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:               
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
            return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
           self.updated_at = datetime.now()
           models.storage.save()

    def to_dict(self):
        my_dictionary = {}
        my_dictionary["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
                if (key == "created_at" or key == "updated_at"):
                        my_dictionary[key] = value.isoformat()
                else:
                       my_dictionary[key] = value
        return my_dictionary
