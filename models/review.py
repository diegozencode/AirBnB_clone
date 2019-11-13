#!/usr/bin/python3
"""
    Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Attributes:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): empty string
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Initialize constructor """
        super().__init__(*args, **kwargs)
