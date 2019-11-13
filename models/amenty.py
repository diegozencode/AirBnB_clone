#!/usr/bin/python3

"""
Amenty Module
"""

from models.base_model import BaseModel


class Amenty(BaseModel):
    """
    Class Amenty
    """

    name = ''


    def __init__(self, *args, **kwargs):
        """
        Method for initialize for Amenity Class
        """
        super().__init__(*args, **kwargs)
