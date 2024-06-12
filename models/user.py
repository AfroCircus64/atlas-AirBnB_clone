#!/usr/bin/python3
"""
This method defines a class named User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This is a class named User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
