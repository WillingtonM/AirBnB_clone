#!/usr/bin/python3
"""
    Unittests for User model.
    Classes for Unittest:
        TestUser_instantiation
        TestUser_save
        TestUser_to_dict
"""
import os
import unittest
import models
from time import sleep
from datetime import datetime
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Testing the instantiation of User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        usr_1 = User()
        usr_2 = User()
        self.assertNotEqual(usr_1.id, usr_2.id)

    def test_two_users_different_created_at(self):
        usr_1 = User()
        sleep(0.05)
        usr_2 = User()
        self.assertLess(usr_1.created_at, usr_2.created_at)

    def test_two_users_different_updated_at(self):
        usr_1 = User()
        sleep(0.05)
        usr_2 = User()
        self.assertLess(usr_1.updated_at, usr_2.updated_at)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = date_t
        usstr = usr.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + date_t_repr, usstr)
        self.assertIn("'updated_at': " + date_t_repr, usstr)

    def test_args_unused(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        usr = User(id="345", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(usr.id, "345")
        self.assertEqual(usr.created_at, date_t)
        self.assertEqual(usr.updated_at, date_t)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Testing the save method of User class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def test_two_saves(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        second_updated_at = usr.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        usr.save()
        self.assertLess(second_updated_at, usr.updated_at)

    def test_save_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_updates_file(self):
        usr = User()
        usr.save()
        usid = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Testing to_dict method of User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_to_dict_contains_added_attributes(self):
        usr = User()
        usr.middle_name = "ALXAfrica"
        usr.my_number = 98
        self.assertEqual("ALXAfrica", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        usr = User()
        us_dict = usr.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        date_t = datetime.today()
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = date_t
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_to_dict_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
