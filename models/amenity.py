#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Basic class for amenities.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        name (str): Name of amenity (in unspecified format).

    Todo:
        * Update FileStorage to manage correctly
        serialization and deserialization of Amenity.

        * Update your command interpreter (console.py)
        to allow show, create, destroy, update and all used with User.
    """
    name = ""
