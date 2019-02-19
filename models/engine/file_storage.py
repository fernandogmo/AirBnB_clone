#!/usr/bin/python3
"""FileStorage class"""
import json
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

    def all(self):
        """Returns the dictionary `__objects`."""

        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with format `<class name>.id`."""

        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects into the JSON file."""

        temp = {}

        for k, v in self.__objects.items():
            temp[k] = v.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as w_file:
            w_file.write(json.dumps(temp))

    def reload(self):
        """Deserializes the JSON file if exists, otherwise do nothing."""

        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        try:
            with open(self.__file_path, "r", encoding="utf-8") as r_file:
                temp = json.load(r_file)
                for k, v in temp.items():
                    temp_v = classes[v["__class__"]](**v)
                    self.__objects[k] = temp_v
        except FileNotFoundError:
            pass
