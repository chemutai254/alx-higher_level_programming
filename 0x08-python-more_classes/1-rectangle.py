#!/usr/bin/python3
# 1-rectangle.py
"""class Rectangle that defines a rctangle based on 0-rectangle.py"""


class Rectangle(object):
    """Defines new class"""
    def __init__(self, width=0, height=0):
        """initializing attributes"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """property for attribute width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setting values to width"""
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

            @property
            def height(self):
                """property for attribute height"""
                return self.__height

            @height.setter
            def height(self, value):
                """setting values to width"""
                if not isinstance(value, int):
                    raise TypeError('height must be an integer')
                if value < 0:
                    raise ValueError('height must be >= 0')
                self.__height = value
