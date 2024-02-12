#!/usr/bin/python3
"""SQUARE CLASS MODULE TO REPRESENT SQUARE SHAPE"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """CLASS SQUARE TO REPRESENT SQUARE SHAPE"""

    def __init__(self, size, x=0, y=0, base_id=None):
        """CLASS CONSTRUCTOR"""
        super().__init__(size, size, x, y, base_id)

    def __str__(self):
        """print square"""
        return f"[Square] ({self.id}) {super().x}/{super().y} \
- {super().width}"

    @property
    def size(self):
        """get size"""
        return super().width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attribtes"""
        if not args:
            for attribute, value in kwargs.items():
                if attribute == "id":
                    self.id = value
                if attribute == "size":
                    if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                    if not value > 0:
                        raise ValueError("width must be > 0")
                    self.width = value
                    self.height = value
                if attribute == "x":
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.x = value
                if attribute == "y":
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.y = value
        try:
            self.id = args[0]
        except IndexError:
            pass
        try:
            if not isinstance(args[1], int):
                raise TypeError("width must be an integer")
            if not args[1] > 0:
                raise ValueError("width must be > 0")
            self.width = args[1]
            self.height = args[1]
        except IndexError:
            pass
        try:
            if not isinstance(args[2], int):
                raise TypeError("x must be an integer")
            if args[2] < 0:
                raise ValueError("x must be >= 0")
            self.x = args[2]
        except IndexError:
            pass
        try:
            if not isinstance(args[3], int):
                raise TypeError("y must be an integer")
            if args[3] < 0:
                raise ValueError("y must be >= 0")
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
