#!/usr/bin/python3
"""UNITTEST OF BASE MODULE"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestOfBase(unittest.TestCase):
    """Testing of Base Class"""
    def setUp(self) -> None:
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_1_nb_obects_initialized(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)
