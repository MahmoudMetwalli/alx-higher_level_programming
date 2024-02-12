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

    def test_0_nb_obects_present(self):
        """test if nb_objects is present"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_1_nb_obects_initialized(self):
        """test if nb_objects is initialized"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_2_create_instance(self):
        """test for behavior if ID attribute"""
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()
        base_75 = Base(75)
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)
        self.assertEqual(base_3.id, 3)
        self.assertEqual(base_75.id, 75)

    def test_3_to_json_string(self):
        """test for to_json_string method"""
        case_a = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        case_b = []
        case_c = None
        print(len(Base.to_json_string(case_a)))
        print(len(str(case_a)))
        self.assertEqual(len(Base.to_json_string(case_a)), len(str(case_a)))
        self.assertEqual(Base.to_json_string(case_a), '[{"x": 2, "width": 10,\
 "id": 1, "height": 7, "y": 8}]')
        self.assertEqual(Base.to_json_string(case_b), "[]")
        self.assertEqual(Base.to_json_string(case_c), "[]")

if __name__ == "__main__":
    unittest.main()
