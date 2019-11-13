#!/usr/bin/python3

"""
Amenity Module
"""


from models.base_name import BaseName


class Amenity(BaseModel):
    """
    Amenity Class
    """
    name = ''


    def __init__(self, *args, **kwargs):
        """
        Method for initialize for Amenity Class
        """
        super().__init__(*args, **kwargs)
