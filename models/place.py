#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Basic class for places.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        email (str): User's email in `<username>@<domainname>.<tld>` format.
        password (str): User password (with unspecified requirements).
        first_name (str): User's first name.
        last_name (str): User's last name.
        city_id (str): empty string: it will be the City.id
        user_id (str): empty string: it will be the User.id
        name (str): empty string
        description (str): empty string
        number_rooms (int): 0
        number_bathrooms (int): 0
        max_guest (int): 0
        price_by_night (int): 0
        latitude (float): 0.0
        longitude (float): 0.0
        amenity_ids list(str): empty list: later used to list of Amenity.id

    Todo:
        * Update FileStorage to manage correctly
        serialization and deserialization of Place.

        * Update your command interpreter (console.py)
        to allow show, create, destroy, update and all used with User.
    """
    city_id: str = ""  # empty string: it will be the City.id
    user_id: str = ""  # empty string: it will be the User.id
    name: str = ""     # empty string
    description: str = ""  # empty string
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list(str) = []
