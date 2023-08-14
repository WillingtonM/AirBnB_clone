#!/usr/bin/python3
"""
    Unittests for Amenity model.
    Classes for Unittest:
        TestAmenity_instantiation
        TestAmenity_save
        TestAmenity_to_dict
"""
import os
import unittest
import models
from time import sleep
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Testing the instantiation of Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_ispublic_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_updated_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_created_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_name_ispublic_class_attribute(self):
        amt = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amt.__dict__)

    def test_2_amenities_unique_ids(self):
        amt_1 = Amenity()
        amt_2 = Amenity()
        self.assertNotEqual(amt_1.id, amt_2.id)

    def test_2_amenities_different_created_at(self):
        amt_1 = Amenity()
        sleep(0.05)
        amt_2 = Amenity()
        self.assertLess(amt_1.created_at, amt_2.created_at)

    def test_2_amenities_different_updated_at(self):
        amt_1 = Amenity()
        sleep(0.05)
        amt_2 = Amenity()
        self.assertLess(amt_1.updated_at, amt_2.updated_at)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        amt = Amenity()
        amt.id = "123456"
        amt.created_at = amt.updated_at = date_t
        amstr = amt.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + date_t_repr, amstr)
        self.assertIn("'updated_at': " + date_t_repr, amstr)

    def test_args_unused(self):
        amt = Amenity(None)
        self.assertNotIn(None, amt.__dict__.values())

    def test_init_with_kwargs(self):
        """instantiation with kwargs method of testing"""
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        amt = Amenity(id="345", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(amt.id, "345")
        self.assertEqual(amt.created_at, date_t)
        self.assertEqual(amt.updated_at, date_t)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Testing the save method of Amenity class."""

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
        amt = Amenity()
        sleep(0.05)
        first_updated_at = amt.updated_at
        amt.save()
        self.assertLess(first_updated_at, amt.updated_at)

    def test_2_saves(self):
        amt = Amenity()
        sleep(0.05)
        first_updated_at = amt.updated_at
        amt.save()
        second_updated_at = amt.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amt.save()
        self.assertLess(second_updated_at, amt.updated_at)

    def test_save_with_arg(self):
        amt = Amenity()
        with self.assertRaises(TypeError):
            amt.save(None)

    def test_save_updates_file(self):
        amt = Amenity()
        amt.save()
        amid = "Amenity." + amt.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Testing to_dict method of Amenity class."""

    def test_to_dicttype(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_todict_correct_keys(self):
        amt = Amenity()
        self.assertIn("id", amt.to_dict())
        self.assertIn("created_at", amt.to_dict())
        self.assertIn("updated_at", amt.to_dict())
        self.assertIn("__class__", amt.to_dict())

    def test_todict_dded_attrb(self):
        amt = Amenity()
        amt.middle_name = "ALXAfrica"
        amt.my_number = 98
        self.assertEqual("ALXAfrica", amt.middle_name)
        self.assertIn("my_number", amt.to_dict())

    def test_todict_datetime_attrb_are_strs(self):
        amt = Amenity()
        am_dict = amt.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_todict_output(self):
        date_t = datetime.today()
        amt = Amenity()
        amt.id = "123456"
        amt.created_at = amt.updated_at = date_t
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat(),
        }
        self.assertDictEqual(amt.to_dict(), tdict)

    def test_contrast_todict_dunder_dict(self):
        amt = Amenity()
        self.assertNotEqual(amt.to_dict(), amt.__dict__)

    def test_todict_with_arg(self):
        amt = Amenity()
        with self.assertRaises(TypeError):
            amt.to_dict(None)


if __name__ == "__main__":
    unittest.main()

