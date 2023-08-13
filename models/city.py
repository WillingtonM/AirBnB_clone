#!/usr/bin/python3
""" a class that initialise special attributes only for cities """
from models.base_model import BaseModel


class City(BaseModel):
    """ *Class City*"""
    state_id = ""
    name = ""
