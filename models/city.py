#!/usr/bin/python3
"""
This module defines the City class, a model representing a city in the application.
"""
from models.base_model import BaseModel
class City(BaseModel):
    """
    The City class represents a city in the application.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""

