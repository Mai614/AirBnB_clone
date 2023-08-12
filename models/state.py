#!/usr/bin/python3
"""
This module defines the State class, a model representing a state in the application.
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    The State class represents a state in the application.

    Attributes:
        name (str): The name of the state.
    """
    name = ""

