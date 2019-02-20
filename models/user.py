#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Basic user class.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Attributes:
        email (str): User's email in `<username>@<domainname>.<tld>` format.
        password (str): User password (with unspecified requirements).
        first_name (str): User's first name.
        last_name (str): User's last name.

    Todo:
        * Update FileStorage to manage correctly
        serialization and deserialization of User.

        * Update your command interpreter (console.py)
        to allow show, create, destroy, update and all used with User.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
