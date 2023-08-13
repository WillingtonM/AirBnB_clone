#!/usr/bin/python3
"""
    Unittests for models/engine/file_storage.py.
    Classes for Unittest:
        TestFileStorage_instantiation
        TestFileStorage_methods
"""
import os
import unittest
import models
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models.place import Place
from models.city import City


class TestFileStorage_instantiation(unittest.TestCase):
    """Testing the instantiation of FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Testing methods of FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_m = BaseModel()
        usr = User()
        st_class = State()
        plc = Place()
        cty = City()
        amn = Amenity()
        rvw = Review()
        models.storage.new(base_m)
        models.storage.new(usr)
        models.storage.new(st_class)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amn)
        models.storage.new(rvw)
        self.assertIn("BaseModel." + base_m.id, models.storage.all().keys())
        self.assertIn(base_m, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + st_class.id, models.storage.all().keys())
        self.assertIn(st_class, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amn.id, models.storage.all().keys())
        self.assertIn(amn, models.storage.all().values())
        self.assertIn("Review." + rvw.id, models.storage.all().keys())
        self.assertIn(rvw, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        st_class = State()
        base_m = BaseModel()
        usr = User()
        plc = Place()
        cty = City()
        amn = Amenity()
        rvw = Review()
        models.storage.new(base_m)
        models.storage.new(usr)
        models.storage.new(st_class)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amn)
        models.storage.new(rvw)
        models.storage.save()
        sv_text = ""
        with open("file.json", "r") as f:
            sv_text = f.read()
            self.assertIn("BaseModel." + base_m.id, sv_text)
            self.assertIn("User." + usr.id, sv_text)
            self.assertIn("State." + st_class.id, sv_text)
            self.assertIn("Place." + plc.id, sv_text)
            self.assertIn("City." + cty.id, sv_text)
            self.assertIn("Amenity." + amn.id, sv_text)
            self.assertIn("Review." + rvw.id, sv_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        st_class = State()
        base_m = BaseModel()
        usr = User()
        plc = Place()
        cty = City()
        amn = Amenity()
        rvw = Review()
        models.storage.new(base_m)
        models.storage.new(usr)
        models.storage.new(st_class)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amn)
        models.storage.new(rvw)
        models.storage.save()
        models.storage.reload()
        objcts = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_m.id, objcts)
        self.assertIn("User." + usr.id, objcts)
        self.assertIn("State." + st_class.id, objcts)
        self.assertIn("Place." + plc.id, objcts)
        self.assertIn("City." + cty.id, objcts)
        self.assertIn("Amenity." + amn.id, objcts)
        self.assertIn("Review." + rvw.id, objcts)

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

