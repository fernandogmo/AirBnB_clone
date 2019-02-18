#!/usr/bin/python3
"""FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage manages instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with format {}.{}
        """

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects into the JSON file
        """

        pass

    def reload(self):
        """Deserializes the JSON file if exists, otherwise do nothing
        """

        classes = {"BaseModel": BaseModel}
        pass
