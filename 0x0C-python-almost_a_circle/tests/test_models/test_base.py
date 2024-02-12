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

    def test_4_save_to_file(self):
        """test for save_to_file method"""
        case_r1_a = Rectangle(10, 7, 2, 8)
        case_r2_a = Rectangle(2, 4)
        case_a = [case_r1_a, case_r2_a]
        case_b = []
        case_c = None
        Rectangle.save_to_file(case_a)
        with open("Rectangle.json", encoding='utf-8') as file_case_a:
            self.assertEqual(len(file_case_a.read()), len('[{"y": 8,\
 "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2\
, "width": 2, "height": 4}]'))
        Square.save_to_file(case_b)
        with open("Square.json", encoding='utf-8') as file_case_b:
            self.assertEqual(len(file_case_b.read()), len("[]"))
        Square.save_to_file(case_c)
        with open("Square.json", encoding='utf-8') as file_case_c:
            self.assertEqual(len(file_case_c.read()), len("[]"))
        Rectangle.save_to_file([])
        with open("Rectangle.json", encoding='utf-8') as file_case_d:
            self.assertEqual(len(file_case_d.read()), len("[]"))

if __name__ == "__main__":
    unittest.main()
