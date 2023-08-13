#!/usr/bin/python3
# the base class for other classes

import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel that defines all common attributes/methods
       for other classes"""
    def __init__(self, *args, **kwargs):
        """initialise basemodel class instances"""
        if kwargs:
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs.keys():
                self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """returns the string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the updated_at and saves a instance to the file storage """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of the instance dictionary"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
