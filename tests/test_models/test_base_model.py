#!/usr/bin/python3
"""
    Unittests for BaseMmodel.
    Classes for Unittest:
        TestBaseModel_instantiation
        TestBaseModel_save
        TestBaseModel_to_dict
"""
import os
import unittest
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Testing the instantiation of BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_ispublic_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_updated_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_created_at_ispublic_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_2_models_unique_ids(self):
        base_m1 = BaseModel()
        base_m2 = BaseModel()
        self.assertNotEqual(base_m1.id, base_m2.id)

    def test_2_models_different_created_at(self):
        base_m1 = BaseModel()
        sleep(0.05)
        base_m2 = BaseModel()
        self.assertLess(base_m1.created_at, base_m2.created_at)

    def test_2_models_different_updated_at(self):
        base_m1 = BaseModel()
        sleep(0.05)
        base_m2 = BaseModel()
        self.assertLess(base_m1.updated_at, base_m2.updated_at)

    def test_str_represent(self):
        date_t = datetime.today()
        date_t_repr = repr(date_t)
        base_m = BaseModel()
        base_m.id = "123456"
        base_m.created_at = base_m.updated_at = date_t
        bm_str = base_m.__str__()
        self.assertIn("[BaseModel] (123456)", bm_str)
        self.assertIn("'id': '123456'", bm_str)
        self.assertIn("'created_at': " + date_t_repr, bm_str)
        self.assertIn("'updated_at': " + date_t_repr, bm_str)

    def test_args_unused(self):
        base_m = BaseModel(None)
        self.assertNotIn(None, base_m.__dict__.values())

    def test_init_with_kwargs(self):
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        base_m = BaseModel(id="345", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(base_m.id, "345")
        self.assertEqual(base_m.created_at, date_t)
        self.assertEqual(base_m.updated_at, date_t)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        base_m = BaseModel("12", id="345", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(base_m.id, "345")
        self.assertEqual(base_m.created_at, date_t)
        self.assertEqual(base_m.updated_at, date_t)


class TestBaseModel_save(unittest.TestCase):
    """Testing the save method of BaseModel class."""

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

    def test_1_save(self):
        base_m = BaseModel()
        sleep(0.05)
        first_updated_at = base_m.updated_at
        base_m.save()
        self.assertLess(first_updated_at, base_m.updated_at)

    def test_2_saves(self):
        base_m = BaseModel()
        sleep(0.05)
        first_updated_at = base_m.updated_at
        base_m.save()
        second_updated_at = base_m.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_m.save()
        self.assertLess(second_updated_at, base_m.updated_at)

    def test_save_with_arg(self):
        base_m = BaseModel()
        with self.assertRaises(TypeError):
            base_m.save(None)

    def test_save_updates_file(self):
        base_m = BaseModel()
        base_m.save()
        bm_id = "BaseModel." + base_m.id
        with open("file.json", "r") as f:
            self.assertIn(bm_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Testing to_dict method of BaseModel class."""

    def test_to_dicttype(self):
        base_m = BaseModel()
        self.assertTrue(dict, type(base_m.to_dict()))

    def test_todict_contains_correct_keys(self):
        base_m = BaseModel()
        self.assertIn("id", base_m.to_dict())
        self.assertIn("created_at", base_m.to_dict())
        self.assertIn("updated_at", base_m.to_dict())
        self.assertIn("__class__", base_m.to_dict())

    def test_todict_contains_added_attrb(self):
        base_m = BaseModel()
        base_m.name = "ALXAfrica"
        base_m.my_number = 98
        self.assertIn("name", base_m.to_dict())
        self.assertIn("my_number", base_m.to_dict())

    def test_todict_datetime_attrb_are_strs(self):
        base_m = BaseModel()
        bm_dict = base_m.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_todict_output(self):
        date_t = datetime.today()
        base_m = BaseModel()
        base_m.id = "123456"
        base_m.created_at = base_m.updated_at = date_t
        t_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': date_t.isoformat(),
            'updated_at': date_t.isoformat()
        }
        self.assertDictEqual(base_m.to_dict(), t_dict)

    def test_contrast_todict_dunder_dict(self):
        base_m = BaseModel()
        self.assertNotEqual(base_m.to_dict(), base_m.__dict__)

    def test_todict_with_arg(self):
        base_m = BaseModel()
        with self.assertRaises(TypeError):
            base_m.to_dict(None)


if __name__ == "__main__":
    unittest.main()

