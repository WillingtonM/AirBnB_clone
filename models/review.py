#!/usr/bin/python3
""" a class that add special attributes specificaly for review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ *Class Review* """
    place_id = ""
    user_id = ""
    text = ""
