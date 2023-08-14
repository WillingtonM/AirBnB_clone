#!/usr/bin/python3
"""
    Unittests for Place model.
    Classes for Unittest:
        TestPlace_instantiation
        TestPlace_save
        TestPlace_to_dict
"""
import os
import unittest
import models
from time import sleep
from datetime import datetime
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Testing the instantiation of Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_ispublic_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plc))
        self.assertNotIn("city_id", plc.__dict__)

    def test_user_id_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plc))
        self.assertNotIn("user_id", plc.__dict__)

    def test_name_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plc))
        self.assertNotIn("name", plc.__dict__)

    def test_description_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plc))
        self.assertNotIn("desctiption", plc.__dict__)

    def test_number_rooms_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plc))
        self.assertNotIn("number_rooms", plc.__dict__)

    def test_number_bathrooms_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plc))
        self.assertNotIn("number_bathrooms", plc.__dict__)

    def test_max_guest_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plc))
        self.assertNotIn("max_guest", plc.__dict__)

    def test_price_by_night_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(plc))
        self.assertNotIn("price_by_night", plc.__dict__)

    def test_latitude_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plc))
        self.assertNotIn("latitude", plc.__dict__)

    def test_longitude_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plc))
        self.assertNotIn("longitude", plc.__dict__)

    def test_amenity_ids_ispublic_class_attribute(self):
        plc = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plc))
        self.assertNotIn("amenity_ids", plc.__dict__)

    def test_2_places_unique_ids(self):
        plc_1 = Place()
        plc_2 = Place()
        self.assertNotEqual(plc_1.id, plc_2.id)

    def test_2_places_different_created_at(self):
        plc_1 = Place()
        sleep(0.05)
        plc_2 = Place()
        self.assertLess(plc_1.created_at, plc_2.created_at)

    def test_2_places_different_updated_at(self):
        plc_1 = Place()
        sleep(0.05)
        plc_2 = Place()
        self.assertLess(plc_1.updated_at, plc_2.updated_at)

    def test_str_representation(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        plc = Place()
        plc.id = "123456"
        plc.created_at = plc.updated_at = date_t
        plstr = plc.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + date_t_repr, plstr)
        self.assertIn("'updated_at': " + date_t_repr, plstr)

    def test_args_unused(self):
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())

    def test_init_with_kwargs(self):
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        plc = Place(id="345", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(plc.id, "345")
        self.assertEqual(plc.created_at, date_t)
        self.assertEqual(plc.updated_at, date_t)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Testing the save method of Place class."""

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
        plc = Place()
        sleep(0.05)
        first_updated_at = plc.updated_at
        plc.save()
        self.assertLess(first_updated_at, plc.updated_at)

    def test_2_saves(self):
        plc = Place()
        sleep(0.05)
        first_updated_at = plc.updated_at
        plc.save()
        second_updated_at = plc.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        plc.save()
        self.assertLess(second_updated_at, plc.updated_at)

    def test_save_with_arg(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.save(None)

    def test_save_updates_file(self):
        plc = Place()
        plc.save()
        plid = "Place." + plc.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Testing to_dict method of Place class."""

    def test_to_dicttype(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_todict_contains_correct_keys(self):
        plc = Place()
        self.assertIn("id", plc.to_dict())
        self.assertIn("created_at", plc.to_dict())
        self.assertIn("updated_at", plc.to_dict())
        self.assertIn("__class__", plc.to_dict())

    def test_todict_contains_added_attrb(self):
        plc = Place()
        plc.middle_name = "ALXAfrica"
        plc.my_number = 98
        self.assertEqual("ALXAfrica", plc.middle_name)
        self.assertIn("my_number", plc.to_dict())

    def test_todict_datetime_attrb_are_strs(self):
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_todict_output(self):
        date_t = datetime.today()
        plc = Place()
        plc.id = "123456"
        plc.created_at = plc.updated_at = date_t
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat(),
        }
        self.assertDictEqual(plc.to_dict(), tdict)

    def test_contrast_todict_dunder_dict(self):
        plc = Place()
        self.assertNotEqual(plc.to_dict(), plc.__dict__)

    def test_todict_with_arg(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)


if __name__ == "__main__":
    unittest.main()
