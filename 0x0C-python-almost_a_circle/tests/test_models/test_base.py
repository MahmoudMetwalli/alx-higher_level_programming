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

    def test_5_from_json_string(self):
        """test for from_json_string method"""
        case_str_a = '[{"height": 4, "width": 10, "id": 89},\
 {"height": 7, "width": 1, "id": 7}]'
        case_str_b = None
        case_list_a = Rectangle.from_json_string(case_str_a)
        case_list_b = Square.from_json_string(case_str_b)
        self.assertTrue(isinstance(case_list_a, list))
        self.assertTrue(isinstance(case_list_b, list))
        self.assertEqual(len(case_list_a), 2)
        self.assertEqual(len(case_list_b), 0)

    def test_6_create(self):
        """test for create method"""
        case_dictionary_a = {"height": 4, "width": 10, "id": 89}
        case_dictionary_a_test = {"height": 4, "width":
                                  10, "id": 89, "x": 0, "y": 0}
        case_r = Rectangle.create(**case_dictionary_a)
        self.assertEqual(len(case_r.to_dictionary()),
                         len(case_dictionary_a_test))

    def test_7_load_from_file(self):
        """test for load_from_file"""
        case_r1_a = Rectangle(10, 7, 2, 8)
        case_r2_a = Rectangle(2, 4)
        case_a = [case_r1_a, case_r2_a]
        case_b = []
        case_c = None
        self.assertEqual(len(Rectangle.load_from_file()), len(case_b))
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
        case_list_a = Rectangle.load_from_file()
        case_list_b = Square.load_from_file()
        self.assertEqual(len(case_list_a), len(case_a))
        self.assertEqual(len(case_list_b), len(case_b))

    def test_8_csv(self):
        """
        test for save_to_file_csv,
          load_from_file_csv and create_csv methods
        """
        case_dictionary_a = {"height": "4", "width": "10", "id": "89"}
        case_dictionary_a_test = {"height": 4, "width":
                                  10, "id": 89, "x": 0, "y": 0}
        case_r = Rectangle.create_csv(**case_dictionary_a)
        self.assertEqual(len(case_r.to_dictionary()),
                         len(case_dictionary_a_test))
        Rectangle.save_to_file_csv([case_r])
        case_list = Rectangle.load_from_file_csv()
        self.assertEqual(case_r.to_dictionary(), case_list[0].to_dictionary())


if __name__ == "__main__":
    unittest.main()
