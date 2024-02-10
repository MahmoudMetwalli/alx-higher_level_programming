#!/usr/bin/python3
"""BASE"""
import json


class Base:
    """BASE CLASS"""
    __nb_objects = 0

    def __init__(self, base_id=None):
        """CLASS CONSTRUCTOR"""
        if base_id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = base_id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        json_list = []
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return json_list
        for dictionary in list_dictionaries:
            if not isinstance(dictionary, dict):
                raise TypeError("Input should be of type dict")
            json_list.append(dictionary)
        return json.dumps(json_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON represntation to a file"""
        file_name = cls.__name__ + ".json"
        dict_list = []
        for instance in list_objs:
            dict_list.append(instance.to_dictionary())
        with open(file_name, 'w', encoding='utf-8') as file_a:
            file_a.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """loads an object form JSON"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        instance = None
        if cls is Rectangle:
            instance = Rectangle(1,1)
        if cls is Square:
            instance = Square(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """loads JSON from file and convert it to object"""
        from models.rectangle import Rectangle
        from models.square import Square
        file_name = cls.__name__ + ".json"
        if cls is Rectangle:
            with open(file_name, encoding='utf-8') as file_a:
                return [Rectangle.create(**dictionary) for dictionary
                        in Rectangle.from_json_string(file_a.read())]
        if cls is Square:
            with open(file_name, encoding='utf-8') as file_a:
                return [Square.create(**dictionary) for dictionary
                        in Square.from_json_string(file_a.read())]
