#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the instance's "updated_at" attribute and saves the instance to storage.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary for JSON serialization.
        Returns:
            dict: A dictionary containing instance attributes.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

