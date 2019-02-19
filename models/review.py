#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Basic class for user reviews of places.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        place_id (str): empty string: later it will be Place.id.
        user_id (str): empty string: later it will be User.id.
        text (str): empty string: later will be content of review.

    Todo:
        * Update FileStorage to manage correctly
        serialization and deserialization of Review.

        * Update your command interpreter (console.py)
        to allow show, create, destroy, update and all used with User.
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
