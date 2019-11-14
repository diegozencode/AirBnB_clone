#!/usr/bin/python3
"""
    Amenity Module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenty

    Attributes:
        name (str): empty string
    """

    name = ''

    def __init__(self, *args, **kwargs):
        """ Method for initialize for Amenity Class"""
        super().__init__(*args, **kwargs)
