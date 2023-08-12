#!/usr/bin/python3
"""
This module defines the Place class, a model representing a place in the application.
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    The Place class represents a place in the application.

    Attributes:
        city_id (str): The ID of the city associated with the place.
        user_id (str): The ID of the user associated with the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of IDs of amenities associated with the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

