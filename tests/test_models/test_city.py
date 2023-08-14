#!/usr/bin/python3
"""
    Unittests for City model.
    Classes for Unittest:
        TestCity_instantiation
        TestCity_save
        TestCity_to_dict
"""
import os
import unittest
import models
from time import sleep
from datetime import datetime
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Testing the instantiation of City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_ispublic_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_ispublic_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cty))
        self.assertNotIn("state_id", cty.__dict__)

    def test_name_ispublic_class_attribute(self):
        cty = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cty))
        self.assertNotIn("name", cty.__dict__)

    def test_2_cities_unique_ids(self):
        cty_1 = City()
        cty_2 = City()
        self.assertNotEqual(cty_1.id, cty_2.id)

    def test_2_cities_different_created_at(self):
        cty_1 = City()
        sleep(0.05)
        cty_2 = City()
        self.assertLess(cty_1.created_at, cty_2.created_at)

    def test_2_cities_different_updated_at(self):
        cty_1 = City()
        sleep(0.05)
        cty_2 = City()
        self.assertLess(cty_1.updated_at, cty_2.updated_at)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = date_t
        cty_str = cty.__str__()
        self.assertIn("[City] (123456)", cty_str)
        self.assertIn("'id': '123456'", cty_str)
        self.assertIn("'created_at': " + date_t_repr, cty_str)
        self.assertIn("'updated_at': " + date_t_repr, cty_str)

    def test_args_unused(self):
        cty = City(None)
        self.assertNotIn(None, cty.__dict__.values())

    def test_init_with_kwargs(self):
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        cty = City(id="345", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(cty.id, "345")
        self.assertEqual(cty.created_at, date_t)
        self.assertEqual(cty.updated_at, date_t)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Testing the save method of City class."""

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

    def test_1_save(self):
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        self.assertLess(first_updated_at, cty.updated_at)

    def test_2_saves(self):
        cty = City()
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        second_updated_at = cty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cty.save()
        self.assertLess(second_updated_at, cty.updated_at)

    def test_save_with_arg(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.save(None)

    def test_save_updates_file(self):
        cty = City()
        cty.save()
        cty_id = "City." + cty.id
        with open("file.json", "r") as f:
            self.assertIn(cty_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Testing to_dict method of City class."""

    def test_to_dicttype(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_todict_contains_correct_keys(self):
        cty = City()
        self.assertIn("id", cty.to_dict())
        self.assertIn("created_at", cty.to_dict())
        self.assertIn("updated_at", cty.to_dict())
        self.assertIn("__class__", cty.to_dict())

    def test_todict_contains_added_attrb(self):
        cty = City()
        cty.middle_name = "ALXAfrica"
        cty.my_number = 98
        self.assertEqual("ALXAfrica", cty.middle_name)
        self.assertIn("my_number", cty.to_dict())

    def test_todict_datetime_attrb_are_strs(self):
        cty = City()
        cty_dict = cty.to_dict()
        self.assertEqual(str, type(cty_dict["id"]))
        self.assertEqual(str, type(cty_dict["created_at"]))
        self.assertEqual(str, type(cty_dict["updated_at"]))

    def test_todict_output(self):
        date_t = datetime.today()
        cty = City()
        cty.id = "123456"
        cty.created_at = cty.updated_at = date_t
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat(),
        }
        self.assertDictEqual(cty.to_dict(), tdict)

    def test_contrast_todict_dunder_dict(self):
        cty = City()
        self.assertNotEqual(cty.to_dict(), cty.__dict__)

    def test_todict_with_arg(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
