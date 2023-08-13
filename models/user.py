#!/usr/bin/python3
""" this file contain a class with special attributes associated with users"""
from models.base_model import BaseModel


class User(BaseModel):
    """ *Class User* """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
