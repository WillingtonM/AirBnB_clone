#!/usr/bin/python3
"""
    Unittests for console.py.
    Unittest classes:
        TestHBNBCommand_prompting
        TestHBNBCommand_show
        TestHBNBCommand_create
        TestHBNBCommand_destroy
        TestHBNBCommand_update
        TestHBNBCommand_count
        TestHBNBCommand_all
        TestHBNBCommand_hlp
        TestHBNBCommand_exit
"""
import os
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommand_prompting(unittest.TestCase):
    """Testing prompting of HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_create(unittest.TestCase):
    """Testing create from HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objcts = {}

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

    def test_create_msng_class(self):
        crct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_create_class_invalid(self):
        crct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_create_invalid_syntx(self):
        crct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(crct, output.getvalue().strip())
        crct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_create_objct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "User.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "State.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "City.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "Place.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_k = "Review.{}".format(output.getvalue().strip())
            self.assertIn(test_k, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Testing show from HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objcts = {}

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

    def test_show_msng_class(self):
        crct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_show_inval_class(self):
        crct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_show_msng_id_spc_notation(self):
        crct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_show_msng_id_dot_notation(self):
        crct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_show_no_inst_found_spc_notation(self):
        crct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_show_no_inst_found_dot_notation(self):
        crct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_show_objcts_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["BaseModel.{}".format(test_ID)]
            cmd = "show BaseModel {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["User.{}".format(test_ID)]
            cmd = "show User {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["State.{}".format(test_ID)]
            cmd = "show State {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Place.{}".format(test_ID)]
            cmd = "show Place {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["City.{}".format(test_ID)]
            cmd = "show City {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Amenity.{}".format(test_ID)]
            cmd = "show Amenity {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Review.{}".format(test_ID)]
            cmd = "show Review {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())

    def test_show_objcts_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["BaseModel.{}".format(test_ID)]
            cmd = "BaseModel.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["User.{}".format(test_ID)]
            cmd = "User.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["State.{}".format(test_ID)]
            cmd = "State.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Place.{}".format(test_ID)]
            cmd = "Place.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["City.{}".format(test_ID)]
            cmd = "City.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Amenity.{}".format(test_ID)]
            cmd = "Amenity.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Review.{}".format(test_ID)]
            cmd = "Review.show({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(c_obj.__str__(), output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Testing destroy from HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objcts = {}

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
        storage.reload()

    def test_destroy_msng_class(self):
        crct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_destroy_inval_class(self):
        crct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_destroy_id_msng_spc_notation(self):
        crct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_destroy_id_msng_dot_notation(self):
        crct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_destroy_invalid_id_spc_notation(self):
        crct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        crct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_destroy_objcts_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["BaseModel.{}".format(test_ID)]
            cmd = "destroy BaseModel {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["User.{}".format(test_ID)]
            cmd = "show User {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["State.{}".format(test_ID)]
            cmd = "show State {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Place.{}".format(test_ID)]
            cmd = "show Place {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["City.{}".format(test_ID)]
            cmd = "show City {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Amenity.{}".format(test_ID)]
            cmd = "show Amenity {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Review.{}".format(test_ID)]
            cmd = "show Review {}".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())

    def test_destroy_objcts_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["BaseModel.{}".format(test_ID)]
            cmd = "BaseModel.destroy({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["User.{}".format(test_ID)]
            cmd = "User.destroy({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["State.{}".format(test_ID)]
            cmd = "State.destroy({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Place.{}".format(test_ID)]
            cmd = "Place.destroy({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["City.{}".format(test_ID)]
            cmd = "City.destroy({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Amenity.{}".format(test_ID)]
            cmd = "Amenity.destroy({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            c_obj = storage.all()["Review.{}".format(test_ID)]
            cmd = "Review.destory({})".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertNotIn(c_obj, storage.all())


class TestHBNBCommand_update(unittest.TestCase):
    """Testing update from HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objcts = {}

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

    def test_update_msng_class(self):
        crct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_inval_class(self):
        crct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_msng_id_spc_notation(self):
        crct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_msng_id_dot_notation(self):
        crct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_invalid_id_spc_notation(self):
        crct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_invalid_id_dot_notation(self):
        crct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_msng_attr_name_spc_notation(self):
        crct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_ID = output.getvalue().strip()
            test_CMD = "update BaseModel {}".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_ID = output.getvalue().strip()
            test_CMD = "update User {}".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_ID = output.getvalue().strip()
            test_CMD = "update State {}".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_ID = output.getvalue().strip()
            test_CMD = "update City {}".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_ID = output.getvalue().strip()
            test_CMD = "update Amenity {}".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_ID = output.getvalue().strip()
            test_CMD = "update Place {}".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_msng_attr_name_dot_notation(self):
        crct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_ID = output.getvalue().strip()
            test_CMD = "BaseModel.update({})".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            test_ID = output.getvalue().strip()
            test_CMD = "User.update({})".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            test_ID = output.getvalue().strip()
            test_CMD = "State.update({})".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            test_ID = output.getvalue().strip()
            test_CMD = "City.update({})".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            test_ID = output.getvalue().strip()
            test_CMD = "Amenity.update({})".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            test_ID = output.getvalue().strip()
            test_CMD = "Place.update({})".format(test_ID)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_msng_attr_value_spc_notation(self):
        crct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update BaseModel {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update User {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update State {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update City {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update Amenity {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update Place {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "update Review {} attr_name".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_msng_attr_value_dot_notation(self):
        crct = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "BaseModel.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "User.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "State.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "City.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "Amenity.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "Place.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_ID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            test_CMD = "Review.update({}, attr_name)".format(test_ID)
            self.assertFalse(HBNBCommand().onecmd(test_CMD))
            self.assertEqual(crct, output.getvalue().strip())

    def test_update_valid_string_attr_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_ID = output.getvalue().strip()
        test_CMD = "update BaseModel {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["BaseModel.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_ID = output.getvalue().strip()
        test_CMD = "update User {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["User.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_ID = output.getvalue().strip()
        test_CMD = "update State {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["State.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_ID = output.getvalue().strip()
        test_CMD = "update City {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["City.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "update Place {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_ID = output.getvalue().strip()
        test_CMD = "update Amenity {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Amenity.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_ID = output.getvalue().strip()
        test_CMD = "update Review {} attr_name 'attr_value'".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Review.{}".format(test_ID)].__dict__
        self.assertTrue("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            t_id = output.getvalue().strip()
        test_CMD = "BaseModel.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["BaseModel.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            t_id = output.getvalue().strip()
        test_CMD = "User.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["User.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            t_id = output.getvalue().strip()
        test_CMD = "State.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["State.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            t_id = output.getvalue().strip()
        test_CMD = "City.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["City.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            t_id = output.getvalue().strip()
        test_CMD = "Place.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Place.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            t_id = output.getvalue().strip()
        test_CMD = "Amenity.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Amenity.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            t_id = output.getvalue().strip()
        test_CMD = "Review.update({}, attr_name, 'attr_value')".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Review.{}".format(t_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attr_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "update Place {} max_guest 98".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_int_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            t_id = output.getvalue().strip()
        test_CMD = "Place.update({}, max_guest, 98)".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Place.{}".format(t_id)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_float_attr_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "update Place {} latitude 7.2".format(test_ID)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_float_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            t_id = output.getvalue().strip()
        test_CMD = "Place.update({}, latitude, 7.2)".format(t_id)
        self.assertFalse(HBNBCommand().onecmd(test_CMD))
        test_dict = storage.all()["Place.{}".format(t_id)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_dictionary_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_ID = output.getvalue().strip()
        test_CMD = "update BaseModel {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["BaseModel.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_ID = output.getvalue().strip()
        test_CMD = "update User {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["User.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_ID = output.getvalue().strip()
        test_CMD = "update State {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["State.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_ID = output.getvalue().strip()
        test_CMD = "update City {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["City.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "update Place {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_ID = output.getvalue().strip()
        test_CMD = "update Amenity {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Amenity.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_ID = output.getvalue().strip()
        test_CMD = "update Review {} ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Review.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            test_ID = output.getvalue().strip()
        test_CMD = "BaseModel.update({}".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["BaseModel.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            test_ID = output.getvalue().strip()
        test_CMD = "User.update({}, ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["User.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            test_ID = output.getvalue().strip()
        test_CMD = "State.update({}, ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["State.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            test_ID = output.getvalue().strip()
        test_CMD = "City.update({}, ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["City.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "Place.update({}, ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            test_ID = output.getvalue().strip()
        test_CMD = "Amenity.update({}, ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Amenity.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            test_ID = output.getvalue().strip()
        test_CMD = "Review.update({}, ".format(test_ID)
        test_CMD += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Review.{}".format(test_ID)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "update Place {} ".format(test_ID)
        test_CMD += "{'max_guest': 98})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "Place.update({}, ".format(test_ID)
        test_CMD += "{'max_guest': 98})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "update Place {} ".format(test_ID)
        test_CMD += "{'latitude': 9.8})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            test_ID = output.getvalue().strip()
        test_CMD = "Place.update({}, ".format(test_ID)
        test_CMD += "{'latitude': 9.8})"
        HBNBCommand().onecmd(test_CMD)
        test_dict = storage.all()["Place.{}".format(test_ID)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class TestHBNBCommand_count(unittest.TestCase):
    """Testing count method of HBNB comand interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objcts = {}

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

    def test_count_inval_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_objct(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


class TestHBNBCommand_all(unittest.TestCase):
    """Testing all of HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objcts = {}

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

    def test_all_inval_class(self):
        crct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(crct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(crct, output.getvalue().strip())

    def test_all_objcts_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objcts_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_single_objct_spc_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_objct_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Testing exiting from HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_hlp(unittest.TestCase):
    """Testing help messages of HBNB command interpreter."""

    def test_hlp_quit(self):
        h_txt, = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_create(self):
        h_txt, = ("Usage: create <class>\n        "
             "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_EOF(self):
        h_txt, = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_show(self):
        h_txt, = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
             "Display the string representation of a class instance of"
             " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_destroy(self):
        h_txt, = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
             "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_all(self):
        h_txt, = ("Usage: all or all <class> or <class>.all()\n        "
             "Display string representations of all instances of a given class"
             ".\n        If no class is specified, displays all instantiated "
             "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_count(self):
        h_txt, = ("Usage: count <class> or <class>.count()\n        "
             "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp_update(self):
        h_txt, = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n       <class>.update(<id>, <dictionary>)\n        "
             "Update a class instance of a given id by adding or updating\n   "
             "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h_txt, output.getvalue().strip())

    def test_hlp(self):
        h_txt, = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h_txt, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
