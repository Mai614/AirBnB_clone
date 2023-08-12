#!/usr/bin/python3
"""
This module defines the Amenity class, a model representing an amenity in the application.
"""
from models.base_model import BaseModel
class Amenity(BaseModel):
    """
    The Amenity class represents an amenity in the application.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

