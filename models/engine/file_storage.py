#!/usr/bin/python3
"""FileStorage class"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage manages instances."""
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """Returns the dictionary `__objects`."""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """Sets obj in __objects with format `<class name>.id`."""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls.__objects[obj_key] = obj

    @classmethod
    def save(cls):
        """Serializes __objects into the JSON file."""
        temp = {}
        for k, v in cls.__objects.items():
            temp[k] = v.to_dict()
        with open(cls.__file_path, "w", encoding="utf-8") as w_file:
            w_file.write(json.dumps(temp))

    @classmethod
    def reload(cls):
        """Deserializes the JSON file if exists, otherwise do nothing."""
        try:
            with open(cls.__file_path, "r", encoding="utf-8") as r_file:
                temp = json.load(r_file)
                for k, v in temp.items():
                    temp_v = models.classes[v["__class__"]](**v)
                    cls.__objects[k] = temp_v
        except FileNotFoundError:
            pass
