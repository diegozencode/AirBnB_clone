#!/usr/bin/python3
"""
    Base model module
"""
from datetime import datetime
import json
import uuid


class BaseModel:
    """
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        """
        i = self.id
        cl = self.__class__.__name__
        d = str(self.__dict__)
        return '[' + cl + '] (' + i + ') ' + d

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        return json.dumps(self.__class__.name, self.id, self.updated_at)
