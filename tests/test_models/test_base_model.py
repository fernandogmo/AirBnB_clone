#!/usr/bin/python3
import unittest
# import pep8
# import inspect  # TODO use like in past proj
from datetime import datetime as dt
from models.base_mode import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    '''
    def setUp(self):
        self.m1 = BaseModel()

    def tearDown(self):
        del self.m1

    def test_module_docstring(self):
        self.assertTrue(0 < len(models.base_model.__doc__), "TODO")

    def test_class_docstring(self):
        self.assertTrue(0 < len(BaseModel.__doc__), "TODO")

    def test_function_docstring(self):
        # TODO get impl from past project. That was pretty.
        pass

    def test_pep8_conformance(self):
        pass

    def test_unique_uuid(self):
        m2 = BaseModel()
        self.assertNotEqual(self.m1.id, m2.id)

    def test_save(self):
        prev_time = self.m1.updated_at
        self.m1.save()
        self.assertNotEqual(prev_time, self.m1.updated_at)
