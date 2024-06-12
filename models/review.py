#!/usr/bin/python3
"""
This module defines a class named Review that inherits from base model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ This is a class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
