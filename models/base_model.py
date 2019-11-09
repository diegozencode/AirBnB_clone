#!/usr/bin/python3

"""
Base Model Module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class Base Model
    """

    def __init__(self):
        """
        Method Init Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """
        Method str for print de class name, id and dictionary
        """
        i = self.id
        cl = self.__class__.__name__
        d = str(self.__dict__)
        return '[' + cl + '] (' + i + ') ' + d

    def save(self):
        """
        Method save for update the attribute with public instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method to_dict for back a dictionary with all key and values
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.__dict__["created_at"].isoformat()
        new_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        return new_dict
