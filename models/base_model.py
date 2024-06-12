#!/usr/bin/python3

from datetime import datetime
import uuid
import models

"""Defines a class BaseModel"""


class BaseModel:
    """Class that defines all common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """instantiation of BaseModel"""
        from models import storage

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                self.first_name = ""
                self.last_name = ""
                self.email = ""
                self.password = ""
                storage.new(self)

    def __str__(self):
        """Returns the string representation"""
        return "[{}] ({})\
 {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instantance attr with current date/time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary of with all key/values of dict"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
