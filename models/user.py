#!/usr/bin/python3

"""
Module User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User whit attribute public
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''


    def __init__(self, *args, **kwargs):
        """Method Constructor with attributes public of user"""
        super().__init__(*args, **kwargs)
