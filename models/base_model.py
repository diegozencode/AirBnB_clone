#!/usr/bin/python3
"""
    Base Model Module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base Model for other classes"""

    def __init__(self, *args, **kwargs):
        """Init Constructor

        Args:
            *args: not used
            **kwargs (dict): attributes
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Method str for print de class name, id and dictionary

        Returns:
            string representation
        """
        i = self.id
        cl = self.__class__.__name__
        d = str(self.__dict__)
        return '[' + cl + '] (' + i + ') ' + d

    def save(self):
        """Save the attributes values"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Method for back a dictionary with all key and values

        Returns:
            dict: new dictionary
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.__dict__["created_at"].isoformat()
        new_dict["updated_at"] = self.__dict__["updated_at"].isoformat()
        return new_dict
