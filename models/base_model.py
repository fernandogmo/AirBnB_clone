#!/usr/bin/python3
import uuid
import datetime as dt


class BaseModel:
    '''
    NOTE: instances of `BaseModel` autoupdate `updated_at` after
          any change through an overriden `__setattr__` method.
    '''
    def __init__(self):
        current_time = dt.datetime.now()
        self.id = str(uuid.uuid4())
        super().__setattr__('created_at', current_time)
        super().__setattr__('updated_at', current_time)

    def __str__(self):
        args = __class__.__name__, self.id, self.__dict__
        return "[{}] ({}) <{}>".format(*args)

    def save(self):
        super().__setattr__('updated_at', dt.datetime.now())

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.save()

    def to_dict(self):
        d = self.__dict__
        d['__class__'] = __class__.__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
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
