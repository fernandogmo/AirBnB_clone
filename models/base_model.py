#!/usr/bin/python3
"""Entry point for BaseModel"""
import uuid
from datetime import datetime
from copy import deepcopy
import models


class BaseModel:
    """Class for BaseModel.

    Instances of `BaseModel` autoupdate `updated_at` after
    any change through an overriden `__setattr__` method.

    """
    def __init__(self, *args, **kwargs):
        """Instantiation for BaseModel.

        Args:
            *args: arguments.
            **kwargs: keyworded arguments.
        """
        # TODO make time_attrs class attribute?
        time_attrs = ('created_at', 'updated_at')
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in time_attrs:  # set time attributes from isoformat strs
                    time_val = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, time_val)
                else:
                    setattr(self, k, v)
        else:
            current_time = datetime.now()
            self.id = str(uuid.uuid4())
            for a in time_attrs:
                setattr(self, a, current_time)
            models.storage.new(self)

    def __str__(self):
        """Magic method for `__str__`

        Format: [<class name>] (<self.id>) <self.__dict__>

        """
        args = self.__class__.__name__, self.id, self.__dict__
        return "[{}] ({}) <{}>".format(*args)

    def save(self):
        """Updates the public instance attr `updated_at`
        with the current datetime.

        """
        super().__setattr__('updated_at', datetime.now())
        models.storage.save()

    '''
    def __setattr__(self, name, value):
        """Magic method for `__setattr__`"""

        self.save()
        super().__setattr__(name, value)
    '''

    def to_dict(self):  # TODO make time_attrs class attribute?
        """Returns a dictionary containing all keys/values of __dict__
        of the instance.

        """
        time_attrs = ('created_at', 'updated_at')
        d = deepcopy(self.__dict__)
        d['__class__'] = self.__class__.__name__
        for k, v in d.items():
            if k in time_attrs:  # set time attributes to isoformat strs
                d[k] = v.isoformat()
        return d


if __name__ == '__main__':
    m = BaseModel()
    print(m, '\n')
    m.name = "Holberton"
    m.num = 89
    print(m, '\n')
    m.save()
    print(m, '\n')
    j = m.to_dict()
    print(j)
    print("JSON of m:")
    for k in j.keys():
        print("\t{}: ({}) - {}".format(k, type(j[k]), j[k]))
