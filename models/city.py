#!/usr/bin/python3
"""
    City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class

    Attributes:
        state_id (str): State.id
        name (str): empty string
    """

    state_id = ''
    name = ''

    def __init__(self, *args, **kwars):
        """ Method for initialize State Class """
        super().__init__(*args, **kwargs)
