#!/usr/bin/python3
# a class that handles our file storage
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ class FileStorage that serializes instances to a JSON file
       and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns a dictionary containing all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ adds new objects to our private class instance 'object'"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ serialize current __objects instance to JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fl:
            dic = {key: obj.to_dict() for key, obj in
                   FileStorage.__objects.items()}
            json.dump(dic, fl)

    def reload(self):
        """ deserialize the JSON file back to the __object instance"""
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fl:
                ld = json.load(fl)
                for key, value in ld.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
