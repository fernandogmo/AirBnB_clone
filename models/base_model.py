#!/usr/bin/python3
import uuid
from datetime import datetime
from copy import deepcopy


class BaseModel:
    '''
    NOTE: instances of `BaseModel` autoupdate `updated_at` after
          any change through an overriden `__setattr__` method.
    '''
    def __init__(self, *args, **kwargs):
        # TODO make time_attrs class attribute?
        time_attrs = ('created_at', 'updated_at')
        if kwargs:
            for k, v in kwargs.items():
                if k in time_attrs:  # set time attributes from isoformat strs
                    time_val = dt.fromisoformat(v)
                    setattr(self, k, time_val)
                else:
                    setattr(self, k, v)
        else:
            current_time = datetime.now()
            self.id = str(uuid.uuid4())
            for a in time_attrs:
                setattr(self, a, current_time)

    def __str__(self):
        args = __class__.__name__, self.id, self.__dict__
        return "[{}] ({}) <{}>".format(*args)

    def save(self):
        super().__setattr__('updated_at', datetime.now())

    def __setattr__(self, name, value):
        self.save()
        super().__setattr__(name, value)

    def to_dict(self):  # TODO make time_attrs class attribute?
        time_attrs = ('created_at', 'updated_at')
        d = deepcopy(self.__dict__)
        d['__class__'] = __class__.__name__
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
