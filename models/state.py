#!/usr/bin/python3
"""Entry point for State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Basic state class.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
         name (str): State name (in unknown format).

    Todo:
        * Update FileStorage to manage correctly
        serialization and deserialization of State.

        * Update your command interpreter (console.py)
        to allow show, create, destroy, update and all used with User.
    """
    name = ""
