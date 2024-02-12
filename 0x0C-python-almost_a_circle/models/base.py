#!/usr/bin/python3
"""BASE CLASS MODULE"""
import json
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps(json_list)
        if not isinstance(list_dictionaries, list):
            raise TypeError("Input should be list of dict")
        for dictionary in list_dictionaries:
            if not isinstance(dictionary, dict):
                raise TypeError("Input should be list of dict")
            json_list.append(dictionary)
        return json.dumps(json_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON represntation to a file"""
        file_name = cls.__name__ + ".json"
        dict_list = []
        if list_objs is not None:
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
            instance = Rectangle(1, 1)
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
        with open(file_name, encoding='utf-8') as file_a:
            if cls is Rectangle:
                return [Rectangle.create(**dictionary) for dictionary
                        in Rectangle.from_json_string(file_a.read())]
            if cls is Square:
                return [Square.create(**dictionary) for dictionary
                        in Square.from_json_string(file_a.read())]

    @classmethod
    def create_csv(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        instance = None
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        if cls is Square:
            instance = Square(1)
        for keys, values in dictionary.items():
            dictionary[keys] = int(values)
        instance.update(**dictionary)
        return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes to csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        file_name = cls.__name__ + ".csv"
        if cls is Rectangle:
            attributes = ["id", "width", "height", "x", "y"]
        if cls is Square:
            attributes = ["id", "size", "x", "y"]
        with open(file_name, 'w', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, attributes)
            csv_writer.writeheader()
            for instance in list_objs:
                csv_writer.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        file_name = cls.__name__ + ".csv"
        with open(file_name, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            if cls is Rectangle:
                return [Rectangle.create_csv(**dictionary) for dictionary
                        in csv_reader]
            if cls is Square:
                return [Square.create_csv(**dictionary) for dictionary
                        in csv_reader]

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
