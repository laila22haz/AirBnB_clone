#!/usr/bin/python3
"""
BaseModel module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """BaseModel class that will serve as a base for the other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        return {
            "__class__": self.__class__.__name__,
            **{
                k: v.isoformat() if isinstance(v, datetime) else
                v for k, v in self.__dict__.items()
               }
        }

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
