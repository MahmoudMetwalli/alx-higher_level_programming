#!/usr/bin/python3
"""RECTANGLE"""
from models.base import Base


class Rectangle(Base):
    """CLASS RECTANGLE"""

    def __init__(self, width, height, x=0, y=0, base_id=None):
        """CLASS CONSTRUCTOR"""
        super().__init__(base_id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width > 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height > 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if not value >= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns rectangle area"""
        return self.__height * self.__width

    def display(self):
        """prints rectangle instance with #"""
        if self.__y:
            for m in range(0, self.__y):
                print()
        for i in range(0, self.__height):
            if self.__x:
                for k in range(0, self.__x):
                    print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """print rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update attribtes"""
        if not args:
            for attribute, value in kwargs.items():
                if attribute == "id":
                    self.id = value
                if attribute == "width":
                    if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                    if not value > 0:
                        raise ValueError("width must be > 0")
                    self.__width = value
                if attribute == "height":
                    if not isinstance(value, int):
                        raise TypeError("height must be an integer")
                    if not value > 0:
                        raise ValueError("height must be > 0")
                    self.__height = value
                if attribute == "x":
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value
                if attribute == "y":
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = value
        try:
            self.id = args[0]
        except IndexError:
            pass
        try:
            if not isinstance(args[1], int):
                raise TypeError("width must be an integer")
            if not args[1] > 0:
                raise ValueError("width must be > 0")
            self.__width = args[1]
        except IndexError:
            pass
        try:
            if not isinstance(args[2], int):
                raise TypeError("height must be an integer")
            if not args[2] > 0:
                raise ValueError("height must be > 0")
            self.__height = args[2]
        except IndexError:
            pass
        try:
            if not isinstance(args[3], int):
                raise TypeError("x must be an integer")
            if args[3] < 0:
                raise ValueError("x must be >= 0")
            self.__x = args[3]
        except IndexError:
            pass
        try:
            if not isinstance(args[4], int):
                raise TypeError("y must be an integer")
            if args[4] < 0:
                raise ValueError("y must be >= 0")
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns dictionary representation"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
