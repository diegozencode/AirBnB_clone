#!/usr/bin/python3
"""
    Place Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class

    Attributes:
        city_id (str): City.id
        user_id (str): User.id
        name (str): empty string
        description (str): empty string
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): max guest capacity
        price_by_night (int): price
        latitude (float): coordanates
        longitud (float): coordanates
        amenity_ids (obj: list of str): list of amenity ids
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Method for initialize Place Class """
        super().__init__(*args, **kwargs)
