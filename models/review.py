#!/usr/bin/python3
"""
This module defines the Review class, a model representing a review in the application.
"""
from models.base_model import BaseModel
class Review(BaseModel):
    """
    The Review class represents a review in the application.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

