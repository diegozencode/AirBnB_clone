#!/usr/bin/python3

"""
File Storage Module
"""

import models.base_model import BaseModel
import json

class FileStorage:
    """
    Class File Storage
    """

    def __init__(self):
        """
        Method Init for constructor class File Storage
        """
        self.__file_path = file.json
        self.__object = {}

    def all(self):
        """
        Method for return the dictionary of the private instance object
        """
        return self.__object

    def new(self, obj):
        """
        Method to set in the private instance __object, the key obj
        have the value class name and id
        """
        self.__object[self.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        Method for serializes __object to the JSON file
        """
        new_dic = {}
        for key, value in self.__object.item():
            new_dic[key] = value.to_dic()

        with open(self.__file_path, "w", encoding='utf-8') as f:
            return(f.write(json.dumps(new_dic))

    def reload(self):
        """
        Method for deserializes to JSON file __object
        if the file exist, if not exist, does nothing
        """
        with open(self.__file_path, mode="r", encoding='utf-8') as f:
            return(json.load(f))
