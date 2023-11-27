#!/usr/bin/python3
"""Module for rectangle"""


class Rectangle:
    """Class for rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle object with width and height
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - Retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter - Sets the value of width
        Args:
            value (int): The value to set as width
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - Retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter - Sets the value of height
        Args:
            value (int): The value to set as height
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
