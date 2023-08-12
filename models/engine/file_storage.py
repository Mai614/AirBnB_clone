#!/usr/bin/python3
"""
This module defines the FileStorage class for serializing and deserializing objects.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    The FileStorage class handles serialization and deserialization of objects.

    Attributes:
        __file_path (str): The path to the JSON file for storing serialized objects.
        __objects (dict): A dictionary to store serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Args:
            obj (BaseModel): The object to be serialized and stored.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serializes and saves objects to the JSON file.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

