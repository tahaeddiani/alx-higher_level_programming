#!/usr/bin/python3
"""rectangle"""


class Rectangle(BaseGeometry):
    """child class of basegeo"""	
    def __init__(self, width, height):
        """rectangle"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
