#!/usr/bin/python3
"""Unittest for FileStorage class"""
import json
import os
import unittest
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import models


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage"""

    def setUp(self):
        """Sets up objs"""
        self.m0 = BaseModel()
        self.m1 = User()
        self.m2 = FileStorage()

    def tearDown(self):
        """Tears down objs"""
        del self.m0
        del self.m1
        del self.m2

    def test_pep8(self):
        """
        Test pep8 conformance.
        https://pep8.readthedocs.io/en/release-1.7.x/advanced.html
        """
        file_msgs = [('models/base_model.py',
                      'Found code style errors in base_model.py.'),
                     ('tests/test_models/test_base_model.py',
                      'Found code style errors in test_base_model.py.')]
        for f, e in file_msgs:
            self.assertEqual(pep8.Checker(f).check_all(), 0, e)

    def test_all(self):
        """Test for all() method"""
        self.assertIsInstance(self.m2.all(), dict)
        self.assertIsNotNone(self.m2.all())

    def test_new(self):
        """Test for new() method"""
        self.assertIsInstance(self.m0, BaseModel)
        self.assertIsInstance(self.m1, User)

    def test_save_file_exists(self):
        """Test for save() method

        Checking if the file exists.
        """
        self.m0.save()
        self.m1.save()
        test_file = os.path.isfile('file.json')
        self.assertTrue(test_file)

    def test_save_read_file(self):
        """Test for save() method

        Checking if format inside file is a dict
        """
        file_name = self.m2._FileStorage__file_path
        with open(file_name, "r", encoding="utf-8") as r_file:
            test = json.loads(r_file.readline())

        self.assertIsInstance(test, dict)

    def test_reload_no_json(self):
        """Test for reload() method

        Checking if can reload() without json file
        """
        file_name = self.m2._FileStorage__file_path
        file_name = str(file_name)
        os.remove(file_name)

        self.assertRaises(FileNotFoundError, self.m2.reload())

    def test_reload_with_json(self):
        """Test for reload() method

        Checking if can reload() on json file
        """
        self.m0.save()
        self.m1.save()
        self.m2.reload()
        instance = self.m2.all()
        key_base = "{}.{}".format('BaseModel', self.m0.id)
        key_user = "{}.{}".format('User', self.m1.id)

        self.assertIsInstance(instance[key_base], BaseModel)
        self.assertIsInstance(instance[key_user], User)
