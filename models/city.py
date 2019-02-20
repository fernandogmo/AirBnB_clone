#!/usr/bin/python3
"""Entry point for City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Basic city class.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        state_id (str): This will be the `State.id`.
        name (str): City name.

    Todo:
        * Update FileStorage to manage correctly
        serialization and deserialization of City.

        * Update your command interpreter (console.py)
        to allow show, create, destroy, update and all used with User.
    """
    state_id = ""
    name = ""
