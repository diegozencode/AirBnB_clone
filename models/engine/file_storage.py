#!/usr/bin/python3
"""
File Storage Module
"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    Class File Storage
    """
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        Method for return the dictionary of the private instance object
        """
        return self.__objects

    def new(self, obj):
        """
        Method to set in the private instance __object, the key obj
        have the value class name and id
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        Method for serializes __object to the JSON file
        """
        new_dic = {}
        for key, value in self.__objects.items():
            new_dic[key] = value.to_dict()

        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(new_dic, f)

    def reload(self):
        """
        Method for deserializes to JSON file __object
        """
        exists = os.path.isfile(self.__file_path)
        if exists:
            with open(self.__file_path, mode="r", encoding='utf-8') as f:
                data_load = json.load(f)
            for dic in data_load.values():
                my_new_class = dic["__class__"]
                del dic["__class__"]
                self.new(eval(my_new_class)(**dic))
